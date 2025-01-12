from enum import Enum

from leafnode import LeafNode


class TextType(Enum):
    """A class for text types of TextNode.

    This class contains text types (enums) for TextNode's text_type param.
    """

    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    """A class to contain different types of text.

    This class as an intermediate representation for converting Markdown text to HTML.

    Attributes:
        test (str): Text content of the node
        text_type (TextType): Type of text
        url (str): Url of the link or image (if the text is link). Default is None.

    """

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, textnode2):
        if (
            self.text == textnode2.text
            and self.text_type == textnode2.text_type
            and self.url == textnode2.url
        ):
            return True
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value
        }, {self.url})"


def text_node_to_html_node(text_node):
    """Convert TextNode to LeafNode

    Args:
        text_node (TextNode): TextNode

    Returns:
        LeafNode: converted TextNode to certain LeafNode type
    """
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            props = {"href": text_node.url}
            return LeafNode("a", text_node.text, None, props)
        case TextType.IMAGE:
            props = {"src": text_node.url, "alt": text_node.text}
            return LeafNode("img", text_node.text, None, props)
        case default:
            raise TypeError(f"Invalid TextType: {text_node.text_type}")
