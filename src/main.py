import os
import shutil
import sys

from copy_files import copy_files
from generate_content import generate_pages_recursively

if sys.argv[0] == "":
    basepath = "/"
else:
    basepath = sys.argv[0]
    print(f"Basepath: {basepath}")

path_static = os.path.expanduser("./static")
path_public = os.path.expanduser("./public")
path_content = os.path.expanduser("./content")
path_template = os.path.expanduser("./template.html")

def main():
    print("Deleting public/ directory...")
    if os.path.exists(path_public):
        shutil.rmtree(path_public)
    
    print(f"\nCopying static files to public dir...")
    copy_files(path_static, path_public)

    print(f"\nGenerating content...")
    generate_pages_recursively(
        basepath,
        path_content, 
        path_template, 
        path_public
    )

    print(f"Generating DONE.\n")
    
if __name__ == "__main__":

    main()
