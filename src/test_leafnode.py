import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leafnode_to_html(self):
        node1 = LeafNode("p", "Content for p leafnode")
        self.assertEqual(node1.to_html(), f"<p>Content for p leafnode</p>")

        props2 = {"href": "https://test.com", "target": "_blank"}
        node2 = LeafNode("a", "Content for a leafnode", None, props2)
        self.assertEqual(
            node2.to_html(),
            f'<a href="https://test.com" target="_blank">Content for a leafnode</a>',
        )

        props3 = {"href": "https://test.com", "target": "_blank"}
        node3 = LeafNode(tag="a", value="Content for a leafnode", props=props3)
        self.assertEqual(
            node3.to_html(),
            f'<a href="https://test.com" target="_blank">Content for a leafnode</a>',
        )

    def test_leafnode_to_html_no_tag(self):
        node1 = LeafNode(None, "Content for empty tag leafnode")
        self.assertEqual(node1.to_html(), f"Content for empty tag leafnode")

    def test_leafnode_to_html_no_value(self):
        try:
            node1 = LeafNode("p", None)
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
        else:
            self.fail("ValueError not raised")

    def test_leafnode_no_children(self):
        children = ["b"]
        props = {"foo": "bar"}
        try:
            node1 = LeafNode(
                tag="p",
                value="Content for leafnode with children",
                children=children,
                props=props,
            )
        except TypeError as e:
            self.assertEqual(type(e), TypeError)
        else:
            self.fail("Type error not raised")

    def test_leafnode_repr(self):
        props = {"href": "https://test.com", "target": "_blank"}
        node1 = LeafNode("a", "Content for leafnode", None, props)
        self.assertEqual(
            repr(node1), f"HTMLNode(a, Content for leafnode, None, {str(props)})"
        )


if __name__ == "__main__":
    unittest.main()
