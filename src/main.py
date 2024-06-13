import os
import shutil

from src.inline import extract_markdown_images, split_nodes_image
from src.textnode import TextNode

def copy_static_to_public() -> None:

    def copy_files(src, dst) -> None:
        print(f"Start copying {src} to {dst}")
        items = os.listdir(src)
        for item in items:
            old_path = src + "/" + item
            new_path = dst + "/" + item
            if os.path.isfile(old_path):
                print(f"Copy {old_path} to {new_path}")
                shutil.copy(old_path, new_path)
            elif os.path.isdir(old_path):
                os.mkdir(new_path)
                copy_files(old_path, new_path)
        return

    if os.path.exists("./public"):
        shutil.rmtree("./public")
    os.mkdir("./public")
    copy_files("./static", "./public")
    return

def main() -> None:
    copy_static_to_public()
    # node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    # print(node)
    
    # extract_markdown_images("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)")
    pass

if __name__ == '__main__':
    main()