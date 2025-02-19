import os
import shutil

from copy_files import copy_files
from generate_content import generate_page

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
    generate_page(
        os.path.join(path_content, "index.md"), 
        path_template, 
        os.path.join(path_public, "index.html")
    )

    print(f"Generating DONE.\n")
    
if __name__ == "__main__":

    main()
