import unittest

from textnode import TextNode, TextType
from textnode_parser import (extract_markdown_images, extract_markdown_links,
                             split_nodes_delimiter)


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


class TestTextNodeParserExtractMarkdownLinks(unittest.TestCase):
    def test_textnode_parsing_extract_markdown_links_valid_input(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        result = extract_markdown_links(node.text)
        expected = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(result, expected)

    def test_textnode_parsing_extract_markdown_links_link_and_image(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev), [to youtube](https://www.youtube.com/@bootdotdev), and image of ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            TextType.TEXT,
        )
        result = extract_markdown_links(node.text)
        expected = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(result, expected)


class TestTextNodeParserExtractMarkdownImages(unittest.TestCase):
    def test_textnode_parsing_extract_markdown_images(self):
        node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            TextType.TEXT,
        )
        result = extract_markdown_images(node.text)
        expected = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertEqual(result, expected)

    def test_textnode_parsing_extract_markdown_images_link_and_image(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev), [to youtube](https://www.youtube.com/@bootdotdev), and image of ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            TextType.TEXT,
        )
        result = extract_markdown_images(node.text)
        expected = [
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
