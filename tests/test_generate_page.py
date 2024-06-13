import unittest

from src.generate_page import extract_title

class TestExtractTitle(unittest.TestCase):
    
    def test_extract_title(self):
        markdown = (
            "# This is the title\n"
            "\n"
            "More texts..."
        )
        markdown_invalid = "Markdown without a title"
        self.assertEqual(extract_title(markdown), "This is the title")
        self.assertRaises(ValueError, extract_title, markdown_invalid)