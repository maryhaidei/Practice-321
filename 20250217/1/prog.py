import os
import sys 

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
