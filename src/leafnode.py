# from .htmlnode import HTMLNode

# class LeafNode(HTMLNode):

#     def __init__(self, value, tag=None, props=None) -> None:
#         super().__init__(tag=tag, value=value, props=props)

#     def to_html(self):
#         return (
#             self.value
#             if self.tag is None
#             else f'<{self.tag}{self.props_to_html()}>{self.value}<\\{self.tag}>'
#         )

#     def __repr__(self) -> str:
#         return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"

# if __name__ == '__main__':
#     node = LeafNode("test text 123", "p", {"test": "test", "test2": "test2"})
#     print(node)
#     print(node.to_html())
#     node2 = LeafNode("test text 123")
#     print(node2.to_html())
