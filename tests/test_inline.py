import unittest

from src.inline import(
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_text_nodes,
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

class TestExtractMarkdownImages(unittest.TestCase):

    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        self.assertEqual(
            extract_markdown_images(text),
            [
                ("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png"),
            ]
        )
                         
class TestExtractMarkdownLinks(unittest.TestCase):

    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        self.assertEqual(
            extract_markdown_links(text),
            [
                ("link", "https://www.example.com"),
                ("another", "https://www.example.com/another"),
            ],
        )

    def test_extract_markdown_links2(self):
        text = "This is the source code and content for the Boot.dev blog, which can be found at [https://blog.boot.dev](https://blog.boot.dev)."
        self.assertEqual(
            extract_markdown_links(text),
            [
                ("https://blog.boot.dev", "https://blog.boot.dev"),
            ],
        )

        
class TestSplitNodesImage(unittest.TestCase):

    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            text_type_text
        )
        self.assertEqual(
            split_nodes_image([node]),
            [
                TextNode("This is text with an ", text_type_text),
                TextNode(
                    "image",
                    text_type_image,
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"
                ),
                TextNode(" and another ", text_type_text),
                TextNode(
                    "second image",
                    text_type_image,
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
                ),
            ],
        )
    
    def test_split_nodes_image_with_duplicate(self):
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and its duplicate ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)",
            text_type_text
        )
        self.assertEqual(
            split_nodes_image([node]),
            [
                TextNode("This is text with an ", text_type_text),
                TextNode(
                    "image",
                    text_type_image,
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"
                ),
                TextNode(" and its duplicate ", text_type_text),
                TextNode(
                    "image",
                    text_type_image,
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"
                ),
            ]
        )
    
    def test_split_nodes_image_more_text(self):
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and more text at the end.",
            text_type_text
        )
        self.assertEqual(
            split_nodes_image([node]),
            [
                TextNode("This is text with an ", text_type_text),
                TextNode(
                    "image",
                    text_type_image,
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"
                ),
                TextNode(" and more text at the end.", text_type_text),
            ]
        )

    def test_split_nodes_image_multiple_nodes(self):
        node1 = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            text_type_text
        )
        node2 = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and more text at the end.",
            text_type_text
        )
        self.assertEqual(
            split_nodes_image([node1, node2,]),
            [
                TextNode("This is text with an ", text_type_text),
                TextNode(
                    "image",
                    text_type_image,
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"
                ),
                TextNode(" and another ", text_type_text),
                TextNode(
                    "second image",
                    text_type_image,
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
                ),
                TextNode("This is text with an ", text_type_text),
                TextNode(
                    "image",
                    text_type_image,
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"
                ),
                TextNode(" and more text at the end.", text_type_text),
            ],
        )
                         
class TestSplitNodesLink(unittest.TestCase):

    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)",
            text_type_text
        )
        self.assertEqual(
            split_nodes_link([node]),
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("link", text_type_link, "https://www.example.com"),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_link, "https://www.example.com/another"),
            ]
        )

    def test_split_nodes_link2(self):
        node = TextNode(
            "This is the source code and content for the Boot.dev blog, which can be found at [https://blog.boot.dev](https://blog.boot.dev).",
            text_type_text
        )
        self.assertEqual(
            split_nodes_link([node]),
            [
                TextNode("This is the source code and content for the Boot.dev blog, which can be found at ", text_type_text),
                TextNode("https://blog.boot.dev", text_type_link, "https://blog.boot.dev"),
                TextNode(".", text_type_text),
            ]
        )

    def test_split_nodes_link_with_duplicate(self):
        node = TextNode(
            "This is text with a [link](https://www.example.com) and its duplicate [link](https://www.example.com)",
            text_type_text
        )
        self.assertEqual(
            split_nodes_link([node]),
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("link", text_type_link, "https://www.example.com"),
                TextNode(" and its duplicate ", text_type_text),
                TextNode("link", text_type_link, "https://www.example.com"),
            ]
        )
    
    def test_split_nodes_link_multiple_nodes(self):
        node1 = TextNode(
            "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)",
            text_type_text
        )
        node2 = TextNode(
            "This is the source code and content for the Boot.dev blog, which can be found at [https://blog.boot.dev](https://blog.boot.dev).",
            text_type_text
        )
        self.assertEqual(
            split_nodes_link([node1, node2]),
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("link", text_type_link, "https://www.example.com"),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_link, "https://www.example.com/another"),
                TextNode("This is the source code and content for the Boot.dev blog, which can be found at ", text_type_text),
                TextNode("https://blog.boot.dev", text_type_link, "https://blog.boot.dev"),
                TextNode(".", text_type_text),
            ]
        )

class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_text_nodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        self.assertEqual(
            text_to_text_nodes(text),
            [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
            ]
        )