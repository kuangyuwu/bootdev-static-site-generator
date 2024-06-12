import re

from src.htmlnode import HTMLNode, LeafNode, ParentNode
from src.inline import text_to_text_nodes
from src.textnode import text_node_to_html_node

block_type_p = "paragraph"
block_type_h = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ul = "unordered_list"
block_type_ol = "ordered_list"

def markdown_to_blocks(markdown: str) -> list[str]:
    blocks: list[str] = []
    lines: list[str] = markdown.split("\n")
    current_block: list[str] = []
    for line in lines:
        if line != "":
            current_block.append(line)
        else:
            if current_block != []:
                block = "\n".join(current_block)
                blocks.append(block.strip())
                current_block = []
    if current_block != []:
        block = "\n".join(current_block)
        blocks.append(block.strip())
    return blocks

def block_to_html_node(block: str) -> HTMLNode:
    block_type = block_to_block_type(block)
    if block_type == block_type_p:
        return paragraph_to_html_node(block)
    elif block_type == block_type_h:
        return heading_to_html_node(block)
    elif block_type == block_type_code:
        return code_to_html_node(block)
    elif block_type == block_type_quote:
        return quote_to_html_node(block)
    elif block_type == block_type_ul:
        return ul_to_html_node(block)
    elif block_type == block_type_ol:
        return ol_to_html_node(block)
    raise Exception("Invalid block type")

def block_to_block_type(block: str) -> str:
    pattern_h = r"#{1,6} .+"
    pattern_code = r"`{3}(.|\n)*`{3}"
    pattern_quote = r">.*(\n>.*)*"
    pattern_ul1 = r"\* .*(\n\* .*)*"
    pattern_ul2 = r"- .*(\n- .*)*"
    pattern_ol = r"\. .*"
    if re.fullmatch(pattern_h, block):
        return block_type_h
    elif re.fullmatch(pattern_code, block):
        return block_type_code
    elif re.fullmatch(pattern_quote, block):
        return block_type_quote
    elif re.fullmatch(pattern_ul1, block) or re.fullmatch(pattern_ul2, block):
        return block_type_ul
    else:
        lines = block.split("\n")
        if all([re.fullmatch(str(i + 1) + pattern_ol, lines[i]) for i in range(len(lines))]):
            return block_type_ol
        else:
            return block_type_p

def paragraph_to_html_node(block: str) -> HTMLNode:
    return ParentNode("p", text_to_children(block))

def heading_to_html_node(block: str) -> HTMLNode:
    for n in range(1, 7):
        if block.startswith(("#" * n) + " "):
            return ParentNode("h" + str(n), [LeafNode(None, block[n + 1:])])

def code_to_html_node(block: str) -> HTMLNode:
    return ParentNode(
        "pre",
        [
            ParentNode(
                "code",
                [LeafNode(None, block[3: -3])]
            )
        ]
    )

def quote_to_html_node(block: str) -> HTMLNode:
    lines = block.split("\n")
    formatted = "\n".join([line[1:] for line in lines])
    return ParentNode("blockquote", text_to_children(formatted))

def ul_to_html_node(block: str) -> HTMLNode:
    lines = block.split("\n")
    children = [ParentNode("li", text_to_children(line[2:])) for line in lines]
    return ParentNode("ul", children)

def ol_to_html_node(block: str) -> HTMLNode:
    lines = block.split("\n")
    children = [ParentNode("li", text_to_children(line.split(" ", 1)[1])) for line in lines]
    return ParentNode("ol", children)

def text_to_children(text: str) -> list[HTMLNode]:
    text_nodes = text_to_text_nodes(text)
    return [text_node_to_html_node(text_node) for text_node in text_nodes]

if __name__ == "__main__":
    block_h1 = "# This is a heading"
    print(heading_to_html_node(block_h1))