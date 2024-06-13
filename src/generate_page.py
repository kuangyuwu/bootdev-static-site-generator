import os

from src.block import markdown_to_html_node

def generate_page_recursive(dir_path_content, template_path, dest_dir_path) -> None:
    items = os.listdir(dir_path_content)
    for item in items:
        from_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(from_path):
            dest_path = dest_path.replace(".md", ".html")
            generate_page(from_path, template_path, dest_path)
        elif os.path.isdir(from_path):
            os.makedirs(dest_path, exist_ok=True)
            generate_page_recursive(from_path, template_path, dest_path)
    return

def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    source_file = open(from_path, "r")
    markdown = source_file.read()
    source_file.close()
    
    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    title = extract_title(markdown)
    content = markdown_to_html_node(markdown).to_html()
    html = template.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", content)
    
    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)
    dest_file = open(dest_path, "w")
    dest_file.write(html)

def extract_title(markdown: str) -> str:
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("Invalid markdown: no title")

if __name__ == "__main__":
    generate_page("./markdown.md", "./template.html", "./testtest.html")