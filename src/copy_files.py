import os
import shutil

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


