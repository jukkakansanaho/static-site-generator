import os
from pathlib import Path
from block_parser import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("Title not found - Markdown must have h1 level title.")

def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} (template: {template_path}) -> {dest_path}")
    from_file = open(from_path, "r")
    md_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(md_content) 
    html = node.to_html()

    title = extract_title(md_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    path_target = os.path.dirname(dest_path)
    if path_target != "":
        os.makedirs(path_target, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)
    to_file.close()

def generate_pages_recursively(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        to_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            to_path = Path(to_path).with_suffix(".html")
            generate_page(from_path, template_path, to_path)
        else:
            generate_pages_recursively(from_path, template_path, to_path)


