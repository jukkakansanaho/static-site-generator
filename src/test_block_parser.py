import unittest
from block_parser import markdown_to_blocks, block_to_block_type

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

    def test_block_parser_block_to_block_type_heading(self):
        text = f"# This is a heading"
        result = block_to_block_type(text)
        expected = "heading"
        self.assertEqual(result, expected)
        
    def test_block_parser_block_to_block_type_code_block(self):
        text = f"```\nThis is a code block line 1\nThis is code block line 2\n```"
        result = block_to_block_type(text)
        expected = "code"
        self.assertEqual(result, expected)

    def test_block_parser_block_to_block_type_quote(self):
        text = f"> This is a quote\n> and quote continues here as well"
        result = block_to_block_type(text)
        expected = "quote"
        self.assertEqual(result, expected)

    def test_block_parser_block_to_block_type_ul_asterisk(self):
        text = f"* This is an unordered list item\n* This is another list item"
        result = block_to_block_type(text)
        expected = "unordered_list"
        self.assertEqual(result, expected)

    def test_block_parser_block_to_block_type_ul_dash(self):
        text = f"- This is an unordered list item\n- This is another list item"
        result = block_to_block_type(text)
        expected = "unordered_list"
        self.assertEqual(result, expected)

    def test_block_parser_block_to_block_type_ordered_list(self):
        text = f"1. This is an ordered list item\n2. This is another ordered list item"
        result = block_to_block_type(text)
        expected = "ordered_list"
        self.assertEqual(result, expected)

    def test_block_parser_block_to_block_type_code_paragraph(self):
        text = f"This is a paragraph"
        result = block_to_block_type(text)
        expected = "paragraph"
        self.assertEqual(result, expected)

    def test_block_parser_block_to_block_type_unclosed_delimiter(self):
        text = f"```This is an invalid code block``"
        result = block_to_block_type(text)
        expected = "paragraph"
        self.assertEqual(result, expected)
        
    def test_block_parser_block_to_block_type_code_text_with_inline_marksdown(self):
        text = f"This is a **bold** text"
        result = block_to_block_type(text)
        expected = "paragraph"
        self.assertEqual(result, expected)

    def test_block_parser_block_to_block_type_subheading(self):
        text = f"###### This is a sub-heading"
        result = block_to_block_type(text)
        expected = "heading"
        self.assertEqual(result, expected)

    
