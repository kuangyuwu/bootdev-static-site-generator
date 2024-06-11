import unittest

from src.inline import(
    split_nodes_delimiter
)
from src.textnode import (
    TextNode,
    text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_link, text_type_image,
)

class TestSplitNodesDelimiter(unittest.TestCase):
    
    def test_split_nodes_delimiter(self):
        nodes = [
            TextNode("aeo;b39 **3ln3 a;sdf9** lak3;l *al;3k h3o* e;j3i `3o3;;bad` ", text_type_text),
            TextNode("epj23 padk3 asd", text_type_bold),
            TextNode(" `3llj` a3ukl.", text_type_text),
        ]
        self.assertEqual(
            split_nodes_delimiter(nodes, "**", text_type_bold),
            [
                TextNode("aeo;b39 ", text_type_text),
                TextNode("3ln3 a;sdf9", text_type_bold),
                TextNode(" lak3;l *al;3k h3o* e;j3i `3o3;;bad` ", text_type_text),
                TextNode("epj23 padk3 asd", text_type_bold),
                TextNode(" `3llj` a3ukl.", text_type_text),
            ]
        )

    def test_split_nodes_delimiter(self):
        nodes = [
                TextNode("aeo;b39 ", text_type_text),
                TextNode("3ln3 a;sdf9", text_type_bold),
                TextNode(" lak3;l *al;3k h3o* e;j3i `3o3;;bad` ", text_type_text),
                TextNode("epj23 padk3 asd", text_type_bold),
                TextNode(" `3llj` a3ukl.", text_type_text),
        ]
        self.assertEqual(
            split_nodes_delimiter(nodes, "*", text_type_italic),
            [
                TextNode("aeo;b39 ", text_type_text),
                TextNode("3ln3 a;sdf9", text_type_bold),
                TextNode(" lak3;l ", text_type_text),
                TextNode("al;3k h3o", text_type_italic),
                TextNode(" e;j3i `3o3;;bad` ", text_type_text),
                TextNode("epj23 padk3 asd", text_type_bold),
                TextNode(" `3llj` a3ukl.", text_type_text),
            ]
        )

    def test_split_nodes_delimiter(self):
        nodes = [
            TextNode("aeo;b39 **3ln3 a;sdf9** lak3;l *al;3k h3o* e;j3i `3o3;;bad` ", text_type_text),
            TextNode("epj23 padk3 asd", text_type_bold),
            TextNode(" `3llj` a3ukl.", text_type_text),
        ]
        self.assertEqual(
            split_nodes_delimiter(nodes, "`", text_type_code),
            [
                TextNode("aeo;b39 **3ln3 a;sdf9** lak3;l *al;3k h3o* e;j3i ", text_type_text),
                TextNode("3o3;;bad", text_type_code),
                TextNode(" ", text_type_text),
                TextNode("epj23 padk3 asd", text_type_bold),
                TextNode(" ", text_type_text),
                TextNode("3llj", text_type_code),
                TextNode(" a3ukl.", text_type_text),
            ]
        )