from .textnode import (
    TextNode,
    text_node_to_html_node,
    text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_link, text_type_image,
)

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



if __name__ == '__main__':
    print("a.b.".split("."))
    # split_nodes_delimiter([TextNode("a.b", text_type_text)], ".", text_type_text)
    nodes = split_nodes_delimiter([TextNode("abc **ad badf** *adf* **ad oepj**", text_type_text)], "**", text_type_bold)
    print(nodes)