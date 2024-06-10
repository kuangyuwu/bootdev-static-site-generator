# import unittest

# from src.leafnode import LeafNode

# class TestLeafNode(unittest.TestCase):

#     def test_to_html(self):
#         node = LeafNode("test text 123", "p", {"prop1": "a", "prop2": "b"})
#         self.assertEqual(node.to_html(), "<p prop1=\"a\" prop2=\"b\">test text 123<\\p>")

#     def test_to_html2(self):
#         node2 = LeafNode("test text 123", "p")
#         self.assertEqual(node2.to_html(), "<p>test text 123<\\p>")

#     def test_to_html3(self):
#         node = LeafNode("test text 123")
#         self.assertEqual(node.to_html(), "test text 123")

#     def test_repr(self):
#         node = LeafNode("test text 123", "p", {"prop1": "a", "prop2": "b"})
#         self.assertEqual(repr(node), "LeafNode(tag=p, value=test text 123, props={'prop1': 'a', 'prop2': 'b'})")