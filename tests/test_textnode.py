import unittest

from src.textnode import TextNode

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

if __name__ == "__main__":
    unittest.main()