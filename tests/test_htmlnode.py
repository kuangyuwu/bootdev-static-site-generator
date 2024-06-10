import unittest

from src.htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):

    def test_repr(self):
        node = HTMLNode()
        self.assertEqual(
            repr(node),
            "HTMLNode(None, None, None, None)"
        )

    def test_repr2(self):
        node = HTMLNode("p", "test", "test", {"prop1": "a", "prop2": "b", "prop3": "c"})
        self.assertEqual(
            repr(node),
            "HTMLNode(p, test, test, {'prop1': 'a', 'prop2': 'b', 'prop3': 'c'})"
        )

    def test_to_html(self):
        node = HTMLNode()
        self.assertRaises(NotImplementedError, node.to_html)
    
    def test_props_to_html(self):
        node = HTMLNode("p", "test", None, {"prop1": "a", "prop2": "b", "prop3": "c"})
        self.assertEqual(node.props_to_html(), ' prop1="a" prop2="b" prop3="c"')

    def test_props_to_html2(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), '')

class TestLeafNode(unittest.TestCase):

    def test_to_html(self):
        node = LeafNode("test text 123", "p", {"prop1": "a", "prop2": "b"})
        self.assertEqual(node.to_html(), "<p prop1=\"a\" prop2=\"b\">test text 123<\\p>")

    def test_to_html2(self):
        node2 = LeafNode("test text 123", "p")
        self.assertEqual(node2.to_html(), "<p>test text 123<\\p>")

    def test_to_html3(self):
        node = LeafNode("test text 123")
        self.assertEqual(node.to_html(), "test text 123")

    def test_repr(self):
        node = LeafNode("test text 123", "p", {"prop1": "a", "prop2": "b"})
        self.assertEqual(repr(node), "LeafNode(tag=p, value=test text 123, props={'prop1': 'a', 'prop2': 'b'})")

if __name__ == "__main__":
    unittest.main()