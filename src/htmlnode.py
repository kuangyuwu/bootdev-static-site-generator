class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        return (
            "".join([f' {key}="{self.props[key]}"' for key in self.props.keys()])
            if self.props is not None
            else ""
        )

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid leaf node: no value")
        return (
            self.value
            if self.tag is None
            else f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        )

    def __repr__(self) -> str:
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid parent node: no tag")
        if not self.children:
            raise ValueError("Invalid parent node: no children")
        contents = []
        for child in self.children:
            contents.append(child.to_html())
        return f"<{self.tag}{self.props_to_html()}>" + "".join(contents) + f"</{self.tag}>"

if __name__ == '__main__':
    node = HTMLNode("test", "test", "test", {"test": "test", "test2": "test2"})
    print(node)
    print(node.props_to_html())
    node2 = HTMLNode()
    print(node2.props_to_html())

    node = LeafNode("p", "test text 123", {"test": "test", "test2": "test2"})
    print(node)
    print(node.to_html())
    node2 = LeafNode(None, "test text 123")
    print(node2.to_html())

    node = ParentNode("p", [LeafNode(None, "test 1"), LeafNode("b", "test 2")], {"prop1": "a", "prop2": "b"})
    print(node.to_html())