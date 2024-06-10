import unittest

from src.htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()