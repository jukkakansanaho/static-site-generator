from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    """A class representing the parent of nested HTMLNodes.

    This class is for any HTML node that isn't a LeafNode (i.e. the parent of LeafNodes/children).

    Attributes:
        tag (str): A string representing the HTML tag name (e.g. "p", "h1", "ol")
        children (list): A list of HTMLNode objects represneting the children of the node.
        props (dict): A dictionary of key-value pairs representing the attributes of the ParentNode.
    """

    def __init__(self, tag, children, props=None):
        # Check if tag is None
        if tag == "" or tag == None:
            raise TypeError("Tag cannot be empty in parentnode")
        # Check if children is None
        if children == [] or children == None:
            raise TypeError("Children cannot be empty in parentnode")
        # Check if tag is an empty string
        if tag is str:
            if self.len(tag) < 1:
                raise ValueError("Tag cannot be empty")
        # Check is children is an empty list
        if children is not None and not isinstance(children, list):
            raise TypeError("Children must be a list or None")
        else:
            if len(children) < 1:
                raise TypeError("Children cannot be empty")

        super().__init__(tag=tag, value=None, children=children, props=props)

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
