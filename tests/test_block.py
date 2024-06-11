import unittest

from src.block import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_p, block_type_h, block_type_code, block_type_quote, block_type_ul, block_type_ol,
)

class TestBlock(unittest.TestCase):

    def test_markdown_to_blocks(self):
        markdown = (
            "  # This is a heading     \n"
            "\n"
            " This is a paragraph of text. It has some **bold** and *italic* words inside of it. \n"
            "\n"
            "\n"
            "    * This is a list item\n"
            "* This is another list item   \n"
        )
        self.assertEqual(
            markdown_to_blocks(markdown),
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                (
                    "* This is a list item\n"
                    "* This is another list item"
                )
            ]
        )
    
    def test_block_to_block_type_p_oneline(self):
        block = "This is **bolded** paragraph"
        self.assertEqual(block_to_block_type(block), block_type_p)
    
    def test_block_to_block_type_p_multline(self):
        block = (
            "This is another paragraph with *italic* text and `code` here.\n"
            "This is the same paragraph on a new line."
        )
        self.assertEqual(block_to_block_type(block), block_type_p)

    def test_block_to_block_type_h1(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), block_type_h)

    def test_block_to_block_type_h2(self):
        block = "## This is a heading"
        self.assertEqual(block_to_block_type(block), block_type_h)

    def test_block_to_block_type_h3(self):
        block = "### This is a heading"
        self.assertEqual(block_to_block_type(block), block_type_h)

    def test_block_to_block_type_h4(self):
        block = "#### This is a heading"
        self.assertEqual(block_to_block_type(block), block_type_h)

    def test_block_to_block_type_h5(self):
        block = "##### This is a heading"
        self.assertEqual(block_to_block_type(block), block_type_h)

    def test_block_to_block_type_h6(self):
        block = "###### This is a heading"
        self.assertEqual(block_to_block_type(block), block_type_h)

    def test_block_to_block_type_h_false(self):
        block = "####### This is a heading"
        self.assertEqual(block_to_block_type(block), block_type_p)
    
    def test_block_to_block_type_code_oneline(self):
        block = r"```console.log(`${a}`)```"
        self.assertEqual(block_to_block_type(block), block_type_code)

    def test_block_to_block_type_code_multline(self):
        block = (
            "```\n"
            "if __name__ == \"__main__\":\n"
            "\tprint(\"hello world\")\n"
            r"\"```\"\n"
            "```"
        )
        self.assertEqual(block_to_block_type(block), block_type_code)
    
    def test_block_to_block_type_code_false(self):
        block = r"```console.log(`${a}`)``"
        self.assertEqual(block_to_block_type(block), block_type_p)

    def test_block_to_block_type_quote_oneline(self):
        block = ">This is a quote."
        self.assertEqual(block_to_block_type(block), block_type_quote)

    def test_block_to_block_type_quote_multline(self):
        block = (
            ">This is a quote\n"
            ">with two lines."
        )
        self.assertEqual(block_to_block_type(block), block_type_quote)

    def test_block_to_block_type_quote_false(self):
        block = (
            ">This is almost a quote\n"
            "Oops"
        )
        self.assertEqual(block_to_block_type(block), block_type_p)

    def test_block_to_block_type_ul1_oneline(self):
        block = "* This is an unordered list"
        self.assertEqual(block_to_block_type(block), block_type_ul)

    def test_block_to_block_type_ul1_multline(self):
        block = (
            "* This is an unordered list\n"
            "* with two items"
        )
        self.assertEqual(block_to_block_type(block), block_type_ul)

    def test_block_to_block_type_ul2_oneline(self):
        block = "- This is an unordered list"
        self.assertEqual(block_to_block_type(block), block_type_ul)

    def test_block_to_block_type_ul2_multline(self):
        block = (
            "- This is an unordered list\n"
            "- with two items"
        )
        self.assertEqual(block_to_block_type(block), block_type_ul)

    def test_block_to_block_type_ul_false(self):
        block = (
            "* This is almost an unordered list\n"
            "Oops"
        )
        self.assertEqual(block_to_block_type(block), block_type_p)

    def test_block_to_block_type_ol_oneline(self):
        block = "1. This is an ordered list"
        self.assertEqual(block_to_block_type(block), block_type_ol)

    def test_block_to_block_type_ol_multline(self):
        block = (
            "1. This is an ordered list\n"
            "2. with two items"
        )
        self.assertEqual(block_to_block_type(block), block_type_ol)

    def test_block_to_block_type_ol_multline2(self):
        block = (
            "1. This is an ordered list\n"
            "2. with a lot of items\n"
            "3. more\n"
            "4. more\n"
            "5. more\n"
            "6. more\n"
            "7. more\n"
            "8. more\n"
            "9. more\n"
            "10. more"
        )
        self.assertEqual(block_to_block_type(block), block_type_ol)

    def test_block_to_block_type_ol_false(self):
        block = (
            "1. This is almost an ordered list\n"
            "3. Oops"
        )
        self.assertEqual(block_to_block_type(block), block_type_p)
