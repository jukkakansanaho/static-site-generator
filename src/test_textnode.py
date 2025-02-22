import unittest

from leafnode import LeafNode
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_textnode_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_textnode_repr(self):

        node1 = TextNode(
            "This is a normal text node", TextType.TEXT, "https://test.com"
        )
        self.assertEqual(
            repr(node1),
            f"TextNode(This is a normal text node, text, https://test.com)",
        )
        node2 = TextNode("This is a bold text node", TextType.BOLD, "https://test.com")
        self.assertEqual(
            repr(node2),
            f"TextNode(This is a bold text node, bold, https://test.com)",
        )
        node3 = TextNode(
            "This is an italic text node", TextType.ITALIC, "https://test.com"
        )
        self.assertEqual(
            repr(node3),
            f"TextNode(This is an italic text node, italic, https://test.com)",
        )

        node4 = TextNode("This is a code text node", TextType.CODE, "https://test.com")
        self.assertEqual(
            repr(node4),
            f"TextNode(This is a code text node, code, https://test.com)",
        )

        node5 = TextNode("This is a link text node", TextType.LINK, "https://test.com")
        self.assertEqual(
            repr(node5),
            f"TextNode(This is a link text node, link, https://test.com)",
        )

    def test_textnode_missing_url(self):

        node1 = TextNode("This is a normal text node without an url", TextType.TEXT)
        self.assertEqual(node1.url, None)

    def test_textnode_text_types(self):
        node1 = TextNode(
            "This is a normal text node", TextType.TEXT, "https://test.com"
        )
        node2 = TextNode(
            "This is an italic text node", TextType.ITALIC, "https://test.com"
        )
        node3 = TextNode("This is a bold text node", TextType.BOLD, "https://test.com")
        node4 = TextNode("This is an code text node", TextType.CODE, "https://test.com")

        node5 = TextNode("This is a link text node", TextType.LINK, "https://test.com")

        self.assertEqual(node1.text_type, TextType.TEXT)
        self.assertEqual(node2.text_type, TextType.ITALIC)
        self.assertEqual(node3.text_type, TextType.BOLD)
        self.assertEqual(node4.text_type, TextType.CODE)
        self.assertEqual(node5.text_type, TextType.LINK)


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_textnode_to_htmlnode_TEXT(self):
        node1 = TextNode("Normal text", TextType.TEXT)
        node2 = LeafNode(None, "Normal text")
        result = text_node_to_html_node(node1)
        self.assertEqual(result, node2)

    def test_textnode_to_htmlnode_BOLD(self):
        node1 = TextNode("Bold text", TextType.BOLD)
        node2 = LeafNode("b", "Bold text")
        result = text_node_to_html_node(node1)
        self.assertEqual(result, node2)

    def test_textnode_to_htmlnode_ITALIC(self):
        node1 = TextNode("Bold text", TextType.ITALIC)
        node2 = LeafNode("i", "Italic text")
        result = text_node_to_html_node(node1)
        self.assertEqual(result, node2)

    def test_textnode_to_htmlnode_CODE(self):
        node1 = TextNode("Code text", TextType.CODE)
        node2 = LeafNode("code", "Code text")
        result = text_node_to_html_node(node1)
        self.assertEqual(result, node2)

    def test_textnode_to_htmlnode_LINK(self):
        node1 = TextNode("Link text", TextType.LINK, "https://test.com")
        props = {"href": "https://test.com"}
        node2 = LeafNode("a", "Link text", None, props)
        result = text_node_to_html_node(node1)
        self.assertEqual(result, node2)

    def test_textnode_to_htmlnode_IMAGE(self):
        node1 = TextNode("Test.com", TextType.IMAGE, "https://test.com/image.jpg")
        props = {"src": "https://test.com/image.jpg", "alt": "Test.com"}
        node2 = LeafNode("img", "Test.com", None, props)
        result = text_node_to_html_node(node1)
        self.assertEqual(result, node2)


if __name__ == "__main__":
    unittest.main()
