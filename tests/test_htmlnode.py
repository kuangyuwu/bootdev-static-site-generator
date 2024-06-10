import unittest

from src.htmlnode import HTMLNode, LeafNode, ParentNode

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
        node = LeafNode("p", "test text 123", {"prop1": "a", "prop2": "b"})
        self.assertEqual(node.to_html(), "<p prop1=\"a\" prop2=\"b\">test text 123</p>")

    def test_to_html_no_props(self):
        node2 = LeafNode("p", "test text 123")
        self.assertEqual(node2.to_html(), "<p>test text 123</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "test text 123")
        self.assertEqual(node.to_html(), "test text 123")

    def test_to_html_no_value(self):
        node = LeafNode(None, None)
        self.assertRaises(ValueError, node.to_html)

    def test_repr(self):
        node = LeafNode("p", "test text 123", {"prop1": "a", "prop2": "b"})
        self.assertEqual(repr(node), "LeafNode(tag=p, value=test text 123, props={'prop1': 'a', 'prop2': 'b'})")
    
class TestParentNode(unittest.TestCase):
    
    def test_to_html_no_tag(self):
        node = ParentNode(None, [], None)
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_no_children(self):
        node = ParentNode("p", [], None)
        self.assertRaises(ValueError, node.to_html)
    
    def test_to_html(self):
        child_node1 = LeafNode("p", "test 1", {"prop1": "a", "prop2": "b"})
        child_node2 = LeafNode("p", "test 2")
        child_node3 = LeafNode(None, "test 3")
        node = ParentNode("div", [child_node1, child_node2, child_node3], {"prop3": "c", "prop4": "d"})
        self.assertEqual(node.to_html(), f"<div prop3=\"c\" prop4=\"d\"><p prop1=\"a\" prop2=\"b\">test 1</p><p>test 2</p>test 3</div>")
    
    def test_to_html_nested(self):
        child_node1 = LeafNode("p", "test 1", {"prop1": "a", "prop2": "b"})
        child_node2 = LeafNode("p", "test 2")
        child_node3 = LeafNode(None, "test 3")
        parent_node = ParentNode("div", [child_node1, child_node2], {"prop3": "c", "prop4": "d"})
        node = ParentNode("div", [child_node3, parent_node], None)
        self.assertEqual(node.to_html(), f"<div>test 3<div prop3=\"c\" prop4=\"d\"><p prop1=\"a\" prop2=\"b\">test 1</p><p>test 2</p></div></div>")

if __name__ == "__main__":
    unittest.main()