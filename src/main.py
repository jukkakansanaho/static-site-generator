import os
import shutil

path_static = os.path.expanduser("./static")
path_public = os.path.expanduser("./public")

def copy_files(source_path, target_path):
    if not os.path.exists(target_path):
        os.mkdir(target_path)

    for file in os.listdir(source_path):
        from_path = os.path.join(source_path, file)
        to_path = os.path.join(target_path, file)
        print(f" * {from_path} -> {to_path}")

        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
        else:
            copy_files(from_path, to_path)

def main():
    print("Deleting public/ directory...")
    if os.path.exists(path_public):
        shutil.rmtree(path_public)
    
    print(f"Copying static files to public dir...")
    copy_files(path_static, path_public)
    print(f"All DONE.")

if __name__ == "__main__":

    main()
