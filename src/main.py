from src.copy_static_to_public import copy_static_to_public
from src.generate_page import generate_page

def main() -> None:
    copy_static_to_public()
    generate_page("./content/index.md", "./template.html", "./public/index.html")
    pass

if __name__ == '__main__':
    main()