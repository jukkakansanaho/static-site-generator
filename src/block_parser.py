import re
from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode
from textnode import TextNode, TextType, text_node_to_html_node
from textnode_parser import text_to_textnodes


block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    """Split markdown text (document) into blocks of markdown.
    Strip empty lines and extra spaces.

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

def text_to_children(text):
    """Converts markdown text to list of LeafNodes.

    Args:
        text (str): A string of markdown text.

    Returns:
        list: A list of LeafNodes with certain TextType.
    """
    text_nodes = text_to_textnodes(text)

    children = []
    for node in text_nodes:
        children.append(text_node_to_html_node(node))

    return children

def text_to_list_type(text, list_type):
    """Converts a text to a list of ParentNodes with tag 'li'.

    Args:
        text (str): A Markdown text string.

    Returns:
        list: A list of ParentNodes with tag 'li'
    """
    pattern = ""
    if list_type == "unordered_list":
        pattern = r"^[*-]\s(.*)$"
    if list_type == "ordered_list":
        pattern = r"^\d+\. +(.+)$"

    # re.MULTILINE applies ^ for start of every line, 
    # not just start of the text string.
    items = re.findall(pattern, text, flags=re.MULTILINE) 
    
    results = []
    for item in items:
        children = text_to_children(item)
        if len(children) > 1:
            results.append(ParentNode(tag="li", children=children))
        else:
            results.append(LeafNode(tag="li", value=item))
    return results

def text_to_code_type(text):
    """Converts text to ParentNode with a code block as LeafNode.

    Args:
        text (str): A Markdown text string.

    Returns:
        ParentNode: A ParentNode with 'pre' tag and within it a LeafNode with 'code' tag.
    """
    return ParentNode(tag="pre", children=[LeafNode(tag="```", value=text)])

def text_to_heading_type(text):
    """Finds heading type (H1-H6) from Markdown text.
        Return HTML heading tag name or None if not a heading. 
    Args:
        text (str): A string to analyse.

    Returns:
        str or None: HTML heading tag (H1-H6) or None if not a heading.
    """
    text = text.strip()

    if not text.startswith("#"):
        return None
    
    heading_symbol_count = 0
    for char in text:
        if char == "#":
            heading_symbol_count += 1
        else:
            break
    if len(text) <= heading_symbol_count or text[heading_symbol_count] != " ":
        return None
    
    return f"h{heading_symbol_count}"

def markdown_to_html_node(markdown):
    """Converts markdown doc into a HTMLNode parent node.

    Args:
        markdown (str): A string in Markdown format

    Returns:
        HTMLNode: A HTMLNode parent node with children nodes.
    """
    markdown_blocks = markdown_to_blocks(markdown)
    block_type_tags = {
        "paragraph": "p",
        "code": "```",
        "unordered_list": "ul",
        "ordered_list": "ol",
        "quote": "blockquote",
        "heading": "heading"
    }

    nodes = []
    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        if block_type == "code":
            nodes.append(text_to_code_type(block))
        if block_type == "unordered_list" or block_type == "ordered_list":
            list_node = text_to_list_type(block, block_type)
            nodes.append(ParentNode(tag=block_type_tags[block_type], children=list_node))
        if block_type == "heading":
            heading_type = text_to_heading_type(block)
            nodes.append(LeafNode(tag=heading_type, value=block))
        else:
            children = text_to_children(block)

            if len(children) > 1:
                nodes.append(ParentNode(tag=block_type_tags[block_type], children=children))
            else:
                nodes.append(LeafNode(tag=block_type_tags[block_type], value=block))
    
    results = ParentNode(tag="div", children=nodes, props=None)
    
    return results



