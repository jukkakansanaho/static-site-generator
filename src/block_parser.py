
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
