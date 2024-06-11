import re

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
    