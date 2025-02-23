import os

def show_git_branches(git_folder):
    heads_dir = os.path.join(git_folder, "refs", "heads")
    if not os.path.isdir(heads_dir):
        print("Нет доступных веток.")
        return
    for root, _, files in os.walk(heads_dir):
        for file in files:
            print(os.path.relpath(os.path.join(root, file), heads_dir))

