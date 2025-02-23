import os
import sys 
import re
import zlib
import binascii

def show_git_branches(git_folder):
    heads_dir = os.path.join(git_folder, "refs", "heads")
    if not os.path.isdir(heads_dir):
        print("Нет доступных веток.")
        return
    for root, _, files in os.walk(heads_dir):
        for file in files:
            print(os.path.relpath(os.path.join(root, file), heads_dir))
            
def load_object(repo_dir, obj_id):
    obj_path = os.path.join(repo_dir, ".git", "objects", obj_id[:2], obj_id[2:])
    try:
        with open(obj_path, "rb") as file:
            compressed_data = file.read()
    except FileNotFoundError:
        sys.exit(f"Не найден объект {obj_id}")
    decompressed_data = zlib.decompress(compressed_data)
    header, _, data = decompressed_data.partition(b'\x00')
    header_text = header.decode("utf-8")
    obj_type, _ = header_text.split(" ", 1)
    return obj_type, data

def extract_commit_info(commit_bytes):
    commit_str = commit_bytes.decode("utf-8", errors="replace")
    header, _, message = commit_str.partition("\n\n")
    info = {"message": message.strip(), "parents": []}
    for line in header.splitlines():
        if line.startswith("tree "):
            info["tree"] = line[5:].strip()
        elif line.startswith("parent "):
            info["parents"].append(line[7:].strip())
        elif line.startswith("author "):
            match = re.match(r"^author\s+(.+ <[^>]+>)", line)
            info["author"] = match.group(1) if match else line[7:].strip()
        elif line.startswith("committer "):
            match = re.match(r"^committer\s+(.+ <[^>]+>)", line)
            info["committer"] = match.group(1) if match else line[10:].strip()
    return info

def display_commit(info):
    print("tree", info.get("tree", ""))
    for parent in info.get("parents", []):
        print("parent", parent)
    print("author", info.get("author", ""))
    print("committer", info.get("committer", ""))
    print()
    print(info.get("message", ""))

def parse_tree_data(tree_bytes):
    items = []
    pos = 0
    while pos < len(tree_bytes):
        space_pos = tree_bytes.find(b' ', pos)
        mode = tree_bytes[pos:space_pos].decode("utf-8")
        pos = space_pos + 1
        null_pos = tree_bytes.find(b'\x00', pos)
        filename = tree_bytes[pos:null_pos].decode("utf-8")
        pos = null_pos + 1
        sha_raw = tree_bytes[pos:pos+20]
        sha_hex = binascii.hexlify(sha_raw).decode("utf-8")
        pos += 20
        kind = "tree" if mode == "40000" else "blob"
        items.append({"mode": mode, "type": kind, "filename": filename, "hash": sha_hex})
    return items

def print_tree_items(items):
    for item in items:
        print(f"{item['type']} {item['hash']}    {item['filename']}")

def walk_history(repo_dir, start_commit):
    current = start_commit
    while current:
        obj_kind, commit_data = load_object(repo_dir, current)
        if obj_kind != "commit":
            sys.exit(f"Объект {current} не является коммитом.")
        commit_info = extract_commit_info(commit_data)
        tree_ref = commit_info.get("tree")
        if not tree_ref:
            sys.exit(f"В коммите {current} отсутствует ссылка на дерево.")
        t_kind, tree_data = load_object(repo_dir, tree_ref)
        if t_kind != "tree":
            sys.exit(f"Объект {tree_ref} не является деревом.")
        tree_items = parse_tree_data(tree_data)
        print(f"TREE for commit {current}")
        print_tree_items(tree_items)
        current = commit_info["parents"][0] if commit_info["parents"] else None

