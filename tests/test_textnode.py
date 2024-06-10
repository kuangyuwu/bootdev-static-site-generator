import unittest

from src.textnode import TextNode, text_node_to_html_node, text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_link, text_type_image
from src.htmlnode import LeafNode

class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("this is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", "bold", "http://test.test")
        node2 = TextNode("This is a text node", "bold", "http://test.test")
        self.assertEqual(node, node2)

    def test_eq_url_false(self):
        node = TextNode("This is a text node", "bold", "http://test.test")
        node2 = TextNode("This is a text node", "bold", "http://test.test2")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "bold", "http://test.test")
        self.assertEqual(
            repr(node),
            "TextNode(This is a text node, bold, http://test.test)"
        )

class TestTextNodeToHTMLNode(unittest.TestCase):

    def test_text_node_to_html_node_text(self):
        text_node = TextNode("Normal text", text_type_text)
        html_node = text_node_to_html_node(text_node)
        html_node2 = LeafNode(None, "Normal text")
        self.assertEqual(html_node.to_html(), html_node2.to_html())

    def test_text_node_to_html_node_bold(self):
        text_node = TextNode("Bold text", text_type_bold)
        html_node = text_node_to_html_node(text_node)
        html_node2 = LeafNode("b", "Bold text")
        self.assertEqual(html_node.to_html(), html_node2.to_html())

    def test_text_node_to_html_node_italic(self):
        text_node = TextNode("Italic text", text_type_italic)
        html_node = text_node_to_html_node(text_node)
        html_node2 = LeafNode("i", "Italic text")
        self.assertEqual(html_node.to_html(), html_node2.to_html())

    def test_text_node_to_html_node_code(self):
        text_node = TextNode("Code text", text_type_code)
        html_node = text_node_to_html_node(text_node)
        html_node2 = LeafNode("code", "Code text")
        self.assertEqual(html_node.to_html(), html_node2.to_html())

    def test_text_node_to_html_node_link(self):
        text_node = TextNode("Link text", text_type_link, "http://www.google.com")
        html_node = text_node_to_html_node(text_node)
        html_node2 = LeafNode("a", "Link text", {"href": "http://www.google.com"})
        self.assertEqual(html_node.to_html(), html_node2.to_html())

    def test_text_node_to_html_node_image(self):
        text_node = TextNode("Image text", text_type_image, "http://www.google.com")
        html_node = text_node_to_html_node(text_node)
        html_node2 = LeafNode("img", "Image text", {"src": "http://www.google.com", "alt": "Image text"})
        self.assertEqual(html_node.to_html(), html_node2.to_html())
        
    def test_text_node_to_html_node_invalid_type(self):
        text_node = TextNode("Normal text", "test")
        self.assertRaises(ValueError, text_node_to_html_node, text_node)

if __name__ == "__main__":
    unittest.main()