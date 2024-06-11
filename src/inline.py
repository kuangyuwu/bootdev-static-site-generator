import re

from .textnode import (
    TextNode,
    text_node_to_html_node,
    text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_link, text_type_image,
)

def text_to_text_nodes(text: str) -> list[TextNode]:
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            result.append(old_node)
        else:
            pieces = old_node.text.split(delimiter)
            if len(pieces) % 2 == 0:
                raise ValueError(f"Invalid md: no closing {delimiter}\n{old_node.text}")
            if len(pieces) == 1:
                result.append(old_node)
            else:
                in_delimiter = False
                for piece in pieces:
                    if in_delimiter:
                        result.append(TextNode(piece, text_type))
                    else:
                        result.append(TextNode(piece, text_type_text))
                    in_delimiter = not in_delimiter
    return result

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    result: list[TextNode] = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            result.append(old_node)
        else:
            text: str = old_node.text
            md_images: list[tuple[str, str]] = extract_markdown_images(text)
            for image_text, image_url in md_images:
                parts: list[str] = text.split(f"![{image_text}]({image_url})", 1)
                result.append(TextNode(parts[0], text_type_text))
                result.append(TextNode(image_text, text_type_image, image_url))
                text = parts[1]
            if text:
                result.append(TextNode(text, text_type_text))
    return result

def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    result: list[TextNode] = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            result.append(old_node)
        else:
            text: str = old_node.text
            md_links: list[tuple[str, str]] = extract_markdown_links(text)
            for link_text, link_url in md_links:
                parts: list[str] = text.split(f"[{link_text}]({link_url})", 1)
                result.append(TextNode(parts[0], text_type_text))
                result.append(TextNode(link_text, text_type_link, link_url))
                text = parts[1]
            if text:
                result.append(TextNode(text, text_type_text))
    return result

def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

if __name__ == '__main__':
    # print("a.b.".split("."))
    # # split_nodes_delimiter([TextNode("a.b", text_type_text)], ".", text_type_text)
    # nodes = split_nodes_delimiter([TextNode("abc **ad badf** *adf* **ad oepj**", text_type_text)], "**", text_type_bold)
    # print(nodes)

    print(split_nodes_link([TextNode(
            "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another) abc",
            text_type_text
        )]))