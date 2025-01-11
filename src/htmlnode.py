class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        if not (isinstance(tag, str) or tag is None):
            raise TypeError("Tag must be a string or None")
        if not (isinstance(value, str) or value is None):
            raise TypeError("Text must be a string or None")
        if children is not None and not isinstance(children, list):
            raise TypeError("Children must be a list or None")
        if props is not None and not isinstance(props, dict):
            raise TypeError("Props must be a dictionary or None")

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag,
            self.value == other.value,
            self.children == other.children,
            self.props == other.props,
        )

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        output = None
        if self.props == {} or self.props == "" or self.props == None:
            output = None
        else:
            output = ""
            for prop in self.props:
                output += f' {prop}="{self.props[prop]}"'
        return output

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
