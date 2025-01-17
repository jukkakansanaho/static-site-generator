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
