import unittest
from generate_content import (
    extract_title,
)

class TestGenerateContent(unittest.TestCase):
    def test_extract_title_valid_title(self):
        md = "# This is h1 level title"
        result = extract_title(md)
        expected = "This is h1 level title"
        self.assertEqual(result, expected)

    def test_extract_title_valid_md(self):
        md = """# This is h1 level title
        
        Here's some text for paragraph.
        """
        result = extract_title(md)
        expected = "This is h1 level title"
        self.assertEqual(result, expected)

    def test_extract_title_invalid_content(self):
        md = "This is title without title-hash"
        try:
            result = extract_title(md)
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
        else:
            self.fail("ValueError not raised")
        

