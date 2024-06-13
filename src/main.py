from src.copy_static_to_public import copy_static_to_public
from src.generate_page import generate_page_recursive

def main() -> None:
    copy_static_to_public()
    generate_page_recursive("./content", "./template.html", "./public")
    pass

if __name__ == '__main__':
    main()