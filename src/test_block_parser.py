import unittest
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from block_parser import (
    markdown_to_blocks,
    markdown_to_html_node,
    block_to_block_type,
    text_to_children,
    paragraph_to_html_node,
    heading_to_html_node,
    code_to_html_node,
    olist_to_html_node,
    ulist_to_html_node,
    quote_to_html_node,
    
)
from parentnode import ParentNode

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

class TestTextToChildren(unittest.TestCase):
    def test_text_to_children_inline_markdown(self):
        node = "Here's some **bold** text.\nAnother line with *italic* text."
        result = text_to_children(node)
        expected = [
            LeafNode(None, "Here's some "),
            LeafNode("b", "bold"),
            LeafNode(None, " text.\nAnother line with "),
            LeafNode("i", "italic"),
            LeafNode(None, " text.")
        ]
        self.assertEqual(result, expected)

    def test_text_to_children_paragraph_markdown(self):
        node = "Here's a basic paragraph."
        result = text_to_children(node)
        expected = [
            LeafNode("p", "Here's a basic pragraph.")
        ]
        self.assertEqual(result, expected)

class TestTextToList(unittest.TestCase):
    def test_text_to_list_ordered_list(self):
        node = "1. list-item-1\n2. list-item-2\n3. list-item-3"
        result = olist_to_html_node(node)
        expected = ParentNode(
            "ol",
            [
            LeafNode("li", "list-item-1"),
            LeafNode("li", "list-item-2"),
            LeafNode("li", "list-item-3"),
            ]
        )
        self.assertEqual(result, expected)

    def test_text_to_list_unordered_list_asterisk(self):
        node = "* list-item\n* list-item\n* list-item"
        result = ulist_to_html_node(node)
        expected = ParentNode(
            "ul",
            [
            LeafNode("li", "list-item"),
            LeafNode("li", "list-item"),
            LeafNode("li", "list-item"),
            ]
        )
        self.assertEqual(result, expected)

    def test_text_to_list_unordered_list_dash(self):
        node = "- list-item\n- list-item\n- list-item"
        result = ulist_to_html_node(node)
        expected = ParentNode(
            "ul", 
            [
            LeafNode("li", "list-item"),
            LeafNode("li", "list-item"),
            LeafNode("li", "list-item"),
            ],
        )
        self.assertEqual(result, expected)


    def test_unordered_list_bold_and_italic(self):
        node = "* list-item with **bold** text\n* list-item with *italic* text\n* list-item with both **bold** and *italic* text"
        result = ulist_to_html_node(node)
        expected = ParentNode(
            "ul",
            [
            ParentNode(
                "li", 
                [
                    LeafNode(None, "list-item with "),
                    LeafNode("b", "bold"),
                    LeafNode(None, " text."),
                ]
            ),
            ParentNode(
                "li",
                [
                    LeafNode(None, "list-item with "),
                    LeafNode("i", "italic"),
                    LeafNode(None, " text."),
                ]
            ),
            ParentNode(
                "li",
                [
                    LeafNode(None, "list-item with both "),
                    LeafNode("b", "bold"),
                    LeafNode(None, " and "),
                    LeafNode("i", "italic"),
                    LeafNode(None, " text.")
                ]
            )
            ]
        )
        self.assertEqual(result, expected)

    def test_text_to_list_invalid_ordered_list(self):
        node = "- list-item\n* list-item\n- list-item"
        result = olist_to_html_node(node)
        expected = ParentNode(
            "ol",
            [
                LeafNode("li", "list-item"),
                LeafNode("li", "list-item"),
                LeafNode("li", "list-item")
            ],
        )
        self.assertEqual(result, expected)

class TestTextToCode(unittest.TestCase):
    def test_text_to_code_valid_input(self):
        node = "```python\nprint('Hello there!')\n# Should print: Hello There!```"
        result = code_to_html_node(node)
        expected = ParentNode(
            "pre",
            [
                LeafNode(
                    "```",
                    "python\nprint('Hello There!')\n#Should print: Hello There!",
                )
            ],
        )
        self.assertEqual(result, expected)

class TestTextToHeading(unittest.TestCase):
     def test_text_to_heading_type_valid_input(self):
        node = "# This is first-level heading\n\nAnd this is paragraph under the heading."
        result = heading_to_html_node(node)
        expected = ParentNode(
            "h1", 
            [
                LeafNode("p", "This is first-level heading"),
            ]
        )
        self.assertEqual(result, expected)

     def test_text_to_heading_type_invalid_input(self):
        node = "This is first-level heading"
        result = heading_to_html_node(node)
        expected = ParentNode(
            "h0", 
            [
                LeafNode("p", "This is first-level heading"),
            ]
        )
        self.assertEqual(result, expected)

class TestMarkdownToHtmlnode(unittest.TestCase):
    def test_markdown_to_htmlnode_valid_input(self):
        node = """
        This is **code** block explaining how to use functions.

        ```python
        text = 'Hello There!'
        print(text)
        ```
        The code above has a couple of things to notice:

        1. Assigning a string to variable named 'text'.
        2. The *string* has content: 'Hello There!'.
        3. Use print() function to **print out** the content of the variable.
        
        > It's not mandatory to assing the content to a variable. You can use: print('Hello There!')
        """

        result = markdown_to_html_node(node)
        expected = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode(None, "This is "),
                        LeafNode("b", "code"),
                        LeafNode(None, " block explaining how to use functions."),
                    ]
                ),
                ParentNode(
                    "pre",
                    [
                        LeafNode("code", "python\ntext = 'Hello There!'\nprint(text)")
                    ]
                ),
                LeafNode("p", "The code above has a couple of things to notice:"),
                ParentNode(
                    "ol",
                    [
                        LeafNode(
                            "li", "Assigning a string to variable named 'text'."
                        ),
                        ParentNode(
                            "li",
                            [
                                LeafNode(None, "The "),
                                LeafNode("i", "string"),
                                LeafNode(None, " has content: 'Hello There!'"),
                            ]
                        ),
                        ParentNode(
                            "li",
                            [
                                LeafNode(None, "Use print() function to "),
                                LeafNode("b", "print out"),
                                LeafNode(None, " the content of the variable.")
                            ]
                        ),
                    ]
                ),
                LeafNode(
                    "blockquote",
                    "It's not mandatory to assign the content to a variable. You can use: print('Hello There!')"
                )
            ]
        )

    def test_markdown_to_html_heading_block(self):
        node = "# This is the first-level heading\n\nThis is a paragraph.\n\n## This is second-level heading\n\nThis is a paragraph.\n\n### This is third-level heading\n\nThis is a paragraph."
        result = markdown_to_html_node(node)
        expected = ParentNode(
           "div",
            [
                LeafNode("h1", "This is the first-level heading"),
                LeafNode("p", "This is a paragraph."),
                LeafNode("h2", "This is second-level heading"),
                LeafNode("p", "This is a paragraph."),
                LeafNode("h3", "This is third-level heading"),
                LeafNode("p", "This is a paragraph."),
            ],
        )
        self.assertEqual(result, expected)

    def test_markdown_to_html_links(self):
        node = "Go [CODING](https://boot.dev)"
        result = markdown_to_html_node(node)
        expected = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode(None, "Go "),
                        LeafNode("a", "CODING", None, {"href": "https://boot.dev"})
                    ],
                )
            ],
        )
        self.assertEqual(result, expected)

class TestMarkdownToHtmlExtra(unittest.TestCase):
    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )
    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )
    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

if __name__ == "__main__":
    unittest.main()
