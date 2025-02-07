import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    """Split markdown text (document) into blocks of markdown.

    Args:
        markdown (str): A markdown document.

    Returns:
        list: A list of markdown blocks.
    """
    blocks = markdown.split("\n\n")

    result = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        result.append(block)
    return result

def block_to_block_type(block):
    """Analyze and define the type of given markdown text block.

    Args:
        block (str): A markdown text block.

    Returns:
        str: a string defining the type of the markdown text block. 
    """
    lines = block.split("\n")
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist
    return block_type_paragraph
