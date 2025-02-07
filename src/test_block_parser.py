import unittest
from block_parser import markdown_to_blocks

class TestBlockParser(unittest.TestCase):
    def test_markdown_to_blocks_valid_markdown(self):
        text = """
            # This is a heading

            This is a paragraph of text. It has some **bold** and *italic* words inside of it.

            * This is the first list item in a list block
            * This is a list item
            * This is another list item
            """
        result = markdown_to_blocks(text)
        expected = [
             "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
            * This is a list item
            * This is another list item"""
        ]
        self.assertEqual(result, expected)

    def test_markdown_parser_empty_string(self):
        text = ""
        result = markdown_to_blocks(text)
        expected = []
        self.assertEqual(result, expected)

    def test_markdown_to_blocks_extra_empty_line(self):
        text = """
            # This is a heading



            This is a paragraph of text. It has some **bold** and *italic* words inside of it.



            * This is the first list item in a list block
            * This is a list item
            * This is another list item
        """
        result = markdown_to_blocks(text)
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
            * This is a list item
            * This is another list item"""
        ]
        self.assertEqual(result, expected)

    def test_markdown_to_blocks_one_block(self):
        text = """
            This is one block of markdown text
        """
        result = markdown_to_blocks(text)
        expected = ["This is one block of markdown text"]
        self.assertEqual(result, expected)


