from src.block import markdown_to_html_node

def extract_title(markdown: str) -> str:
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("Invalid markdown: no title")

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
    
    dest_file = open(dest_path, "w")
    dest_file.write(html)
    pass 

if __name__ == "__main__":
    generate_page("./markdown.md", "./template.html", "./testtest.html")