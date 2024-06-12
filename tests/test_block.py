import unittest

from src.block import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_p, block_type_h, block_type_code, block_type_quote, block_type_ul, block_type_ol,
    block_to_html_node,
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
        block = "####### This is not a heading"
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
        block = "`print(\"hello world\")`"
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

    def test_block_to_html_node_p(self):
        block_p = "This is **bolded** paragraph"
        block_p2 = (
            "This is another paragraph with *italic* text and `code` here.\n"
            "This is the same paragraph on a new line."
        )
        self.assertEqual(
            block_to_html_node(block_p).to_html(),
            "<p>This is <b>bolded</b> paragraph</p>"
        )
        self.assertEqual(
            block_to_html_node(block_p2).to_html(),
            (
                "<p>This is another paragraph with <i>italic</i> text and <code>code</code> here.<br>"
                "This is the same paragraph on a new line.</p>"
            )
        )
    
    def test_block_to_html_node_h(self):
        block_h1 = "# This is a heading"
        block_h2 = "## This is a heading"
        block_h3 = "### This is a heading"
        block_h4 = "#### This is a heading"
        block_h5 = "##### This is a heading"
        block_h6 = "###### This is a heading"
        block_h_fake = "####### This is not a heading"
        self.assertEqual(block_to_html_node(block_h1).to_html(), "<h1>This is a heading</h1>")
        self.assertEqual(block_to_html_node(block_h2).to_html(), "<h2>This is a heading</h2>")
        self.assertEqual(block_to_html_node(block_h3).to_html(), "<h3>This is a heading</h3>")
        self.assertEqual(block_to_html_node(block_h4).to_html(), "<h4>This is a heading</h4>")
        self.assertEqual(block_to_html_node(block_h5).to_html(), "<h5>This is a heading</h5>")
        self.assertEqual(block_to_html_node(block_h6).to_html(), "<h6>This is a heading</h6>")
        self.assertEqual(block_to_html_node(block_h_fake).to_html(), "<p>####### This is not a heading</p>")
    
    def test_block_to_html_node_code(self):
        block_code = r"```console.log(`${a}`)```"
        block_code1 = (
            "```\n"
            "if __name__ == \"__main__\":\n"
            "\tprint(\"hello world\", 3 * 2 * 1)\n"
            r"\"```\"\n"
            "```"
        )
        block_code_fake = "`print(\"hello world\")`"
        self.assertEqual(block_to_html_node(block_code).to_html(), r"<pre><code>console.log(`${a}`)</code></pre>")
        self.assertEqual(
            block_to_html_node(block_code1).to_html(),
            (
                "<pre><code>\n"
                "if __name__ == \"__main__\":\n"
                "\tprint(\"hello world\", 3 * 2 * 1)\n"
                r"\"```\"\n"
                "</code></pre>"
            )
        )
        self.assertEqual(block_to_html_node(block_code_fake).to_html(), "<p><code>print(\"hello world\")</code></p>")
    
    def test_block_to_html_node_quote(self):
        block_quote = ">This is a quote with *italic* text, some `code`, and **bold** text."
        block_quote_2 = (
            ">This is a quote\n"
            ">with two lines."
        )
        block_quote_fake = (
            ">This is almost a quote\n"
            "Oops"
        )
        self.assertEqual(block_to_html_node(block_quote).to_html(), "<blockquote>This is a quote with <i>italic</i> text, some <code>code</code>, and <b>bold</b> text.</blockquote>")
        self.assertEqual(block_to_html_node(block_quote_2).to_html(), "<blockquote>This is a quote<br>with two lines.</blockquote>")
        self.assertEqual(block_to_html_node(block_quote_fake).to_html(), "<p>>This is almost a quote<br>Oops</p>")
    
    def test_block_to_html_node_ul(self):
        block_ul1 = "* This is an **unordered** list"
        block_ul2 = (
            "* This is an **unordered** list\n"
            "* with *two items*"
        )
        block_ul3 = "- This is an **unordered** list"
        block_ul4 = (
            "- This is an **unordered** list\n"
            "- with *two items*"
        )
        block_ul_fake = (
            "- This is almost an unordered list\n"
            "Oops"
        )
        self.assertEqual(block_to_html_node(block_ul1).to_html(), "<ul><li>This is an <b>unordered</b> list</li></ul>")
        self.assertEqual(block_to_html_node(block_ul2).to_html(), "<ul><li>This is an <b>unordered</b> list</li><li>with <i>two items</i></li></ul>")
        self.assertEqual(block_to_html_node(block_ul3).to_html(), "<ul><li>This is an <b>unordered</b> list</li></ul>")
        self.assertEqual(block_to_html_node(block_ul4).to_html(), "<ul><li>This is an <b>unordered</b> list</li><li>with <i>two items</i></li></ul>")
        self.assertEqual(block_to_html_node(block_ul_fake).to_html(), "<p>- This is almost an unordered list<br>Oops</p>")
    
    def test_block_to_html_node_ol(self):
        block_ol1 = "1. This is an **ordered** list"
        block_ol2 = (
            "1. This is an **ordered** list\n"
            "2. with *two items*"
        )
        block_ol3 = (
            "1. This is an **ordered** list\n"
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
        block_ol_fake = (
            "1. This is almost an ordered list\n"
            "3. Oops"
        )
        self.assertEqual(block_to_html_node(block_ol1).to_html(), "<ol><li>This is an <b>ordered</b> list</li></ol>")
        self.assertEqual(block_to_html_node(block_ol2).to_html(), "<ol><li>This is an <b>ordered</b> list</li><li>with <i>two items</i></li></ol>")
        self.assertEqual(block_to_html_node(block_ol3).to_html(), "<ol><li>This is an <b>ordered</b> list</li><li>with a lot of items</li><li>more</li><li>more</li><li>more</li><li>more</li><li>more</li><li>more</li><li>more</li><li>more</li></ol>")
        self.assertEqual(block_to_html_node(block_ol_fake).to_html(), "<p>1. This is almost an ordered list<br>3. Oops</p>")