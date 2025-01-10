from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, children=None, props=None):
        if children != None:
            raise TypeError("Children not allowed in leafnode")
        super().__init__(tag, value, children, props)

    def to_html(self):
        if not self.value or self.value == None:
            raise ValueError("Missing value in leafnode")
        if not self.tag or self.tag == None:
            return self.value
        if not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    # def __repr__(self):
    # return f"LeafNode({self.tag}, {self.value}, None, {str(self.props)}"
