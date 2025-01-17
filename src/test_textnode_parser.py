import unittest

from textnode import TextNode, TextType
from textnode_parser import split_nodes_delimiter


class TestTextNodeParser(unittest.TestCase):
    def test_textnode_parsing_TEXT(self):
        node = TextNode("Text without any delimiter", TextType.TEXT)
        result = split_nodes_delimiter([node], "", TextType.TEXT)
        expected = [TextNode("Text without any delimiter", TextType.TEXT)]
        self.assertEqual(result, expected)

    def test_textnode_parsing_BOLD(self):
        node = TextNode("Text with a **bold text** as a part of it", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("Text with a ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(" as a part of it", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_textnode_parsing_ITALIC(self):
        node = TextNode("Text with an *italic text* as a part of it", TextType.TEXT)
        result = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected = [
            TextNode("Text with an ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC),
            TextNode(" as a part of it", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_textnode_parsing_CODE(self):
        node = TextNode("Text with a `code block` as a part of it", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("Text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" as a part of it", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_textnode_parsing_BOLD_multiple(self):
        node1 = TextNode(
            "Some text with **some bold text** as a part of it", TextType.TEXT
        )
        node2 = TextNode(
            "Another text with **another bold text** as a part of it too", TextType.TEXT
        )
        result = split_nodes_delimiter([node1, node2], "**", TextType.BOLD)
        expected = [
            TextNode("Some text with ", TextType.TEXT),
            TextNode("some bold text", TextType.BOLD),
            TextNode(" as a part of it", TextType.TEXT),
            TextNode("Another text with ", TextType.TEXT),
            TextNode("another bold text", TextType.BOLD),
            TextNode(" as a part of it too", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_textnode_parsing_empty_text(self):
        node = TextNode("**", TextType.TEXT)
        try:
            result = split_nodes_delimiter([node], "**", TextType.BOLD)
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
        else:
            self.fail("ValueError not raised")

    def test_textnode_parsing_no_node(self):
        try:
            result = split_nodes_delimiter(["not a node"], "**", TextType.BOLD)
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
        else:
            self.fail("ValueError not raised")

    def test_textnode_parsing_invalid_nodes_type(self):
        try:
            result = split_nodes_delimiter("not a list", "**", TextType.BOLD)
        except TypeError as e:
            self.assertEqual(type(e), TypeError)
        else:
            self.fail("TypeError not raised")

    def test_textnode_parsing_invalid_text_type(self):
        node = TextNode("Text with bold text as a part of it", TextType.TEXT)
        try:
            result = split_nodes_delimiter([node], "**", "Not a valid TextType")
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
        else:
            self.fail("ValueError not raised")


if __name__ == "__main__":
    unittest.main()
