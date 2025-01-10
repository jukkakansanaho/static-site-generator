from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag == "" or tag == None:
            raise TypeError("Tag required in parentnode")
        if children == [] or children == None:
            raise TypeError("Children required in parentnode")
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == "" or self.tag == None:
            raise ValueError("Missing value in parentnode")
        if len(self.children) == 0 or self.children == None:
            raise ValueError("Missing children in parentnode")

        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        if self.props is None:
            return f"<{self.tag}>{children_html}</{self.tag}>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
