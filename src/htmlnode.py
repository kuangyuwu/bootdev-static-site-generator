class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        return " ".join([f'{key}="{self.props[key]}"' for key in self.props.keys()])

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
        
if __name__ == '__main__':
    node = HTMLNode("test", "test", "test", {"test": "test", "test2": "test2"})
    print(node)
    print(node.props_to_html())