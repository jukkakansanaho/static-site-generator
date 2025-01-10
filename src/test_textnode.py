import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
