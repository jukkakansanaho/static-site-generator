import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """Split TextNode based on delimiter and text_type.
    Args:
        old_nodes (list): List of TextNodes
        delimiter (str): Delimiter for markdown syntax (e.g. * for italic, ** for bold, ` (backtick) for code)
        text_type (TextType): text type of TextNode (e.g. TextType.TEXT, TextType.ITALIC, etc)

    Returns:
        list: List of node split based on delimiter.
    """
    if not isinstance(old_nodes, list):
        raise TypeError("Nodes must be a list")
    if len(old_nodes) == 0:
        return []
    if not isinstance(delimiter, str):
        raise TypeError("Delimiter must be a string")
    if not isinstance(text_type, TextType):
        raise ValueError("Text_type must be a TextType")

    results = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            raise ValueError("Node must be an instance of TextNode class")
        if node.text_type != TextType.TEXT:
            results.append(node)
            continue
        if delimiter == "":
            results.append(node)
            continue

        splitted_nodes = []
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError("Invalid input - delimited part not closed")
        for part in range(len(parts)):
            if parts[part] == "":
                continue
            if part % 2 == 0:
                splitted_nodes.append(TextNode(parts[part], TextType.TEXT))
            else:
                splitted_nodes.append(TextNode(parts[part], text_type))
        results.extend(splitted_nodes)
    return results

def split_nodes_image(old_nodes):
    """Split TextNodes into text (TextType.TEXT) and images (TextType.IMAGE) with alt and url.

    Args:
        old_node (list): list of TextNodes

    Return:
        list: list of TextNodes with TextType.TEXT and TextType.IMAGE.
    """
    if not isinstance(old_nodes, list):
        raise TypeError("Nodes must be a list")
    if len(old_nodes) == 0:
        return []
    
    results = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            raise TypeError("Node must be an instance of TextNode class")
        if node.text_type != TextType.TEXT:
            results.append(node)
            continue

        orig_text = node.text
        parts = extract_markdown_images(orig_text)
        if len(parts) == 0: # Check if IMAGE nodes found
            results.append(node)
            continue

        current_position = 0
        for alt, link in parts:
            img_markup = f"![{alt}]({link})"
            start_index = orig_text.find(img_markup, current_position)
            
            # Add text before IMAGE as a TEXT node
            if start_index > current_position:
                preceding_text = orig_text[current_position:start_index]
                if preceding_text: # Check if text != ""
                    results.append(TextNode(preceding_text, TextType.TEXT))
            # Add IMAGE node
            results.append(TextNode(alt, TextType.IMAGE, link))
            current_position = start_index + len(img_markup)
            
        # Add remaining text as TEXT node
        if current_position < len(orig_text):
            remaining_text = orig_text[current_position:]
            if remaining_text: # Check if text != ""
                results.append(TextNode(remaining_text, TextType.TEXT))

    return results

def split_nodes_link(old_nodes):
    pass


def extract_markdown_images(text):
    """Finds all markdown image links in the text.

    Args:
        text (str): markdown text with image links

    Return:
        list: list of tuples with image alt and url
    """
    pattern = r"!\[([^\[\]]+)\]\(([^()\s]+)\)"
    result = re.findall(pattern, text)
    return result


def extract_markdown_links(text):
    """Finds all markdown links in the text.

    Args:
        text (str): markdown text with links

    Return:
        list: list of tuples with link anchor text and url
    """
    pattern = r"(?<!\!)\[([^\[\]]+)\]\(([^()\s]+)\)"
    result = re.findall(pattern, text)
    return result
