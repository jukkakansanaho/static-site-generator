import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_htmlnode_param_types(self):

        children = [].append(HTMLNode("b", "Content for bold Leafnode"))
        # props = {}
        props = {"href": "https://test.com", "target": "_blank"}
        node1 = HTMLNode("a", "Content for a htmlnode", children, props)

        self.assertIn(type(node1.tag), [str, type(None)])
        self.assertIn(type(node1.value), [str, type(None)])
        self.assertIn(type(node1.children), [list, type(None)])
        self.assertIn(type(node1.props), [dict, type(None)])

    def test_htmlnode_repr_p(self):
        node1 = HTMLNode("p", "Content for p tag")
        self.assertEqual(repr(node1), f"HTMLNode(p, Content for p tag, None, None)")

    def test_htmlnode_repr_a(self):
        props = {"href": "https://test.com"}
        node2 = HTMLNode("a", "Test.com", None, props)
        self.assertEqual(repr(node2), f"HTMLNode(a, Test.com, None, {str(props)})")

        props2 = {"href": "https://test.com", "target": "_blank"}
        node3 = HTMLNode("a", "Test.com", None, props2)
        self.assertEqual(repr(node3), f"HTMLNode(a, Test.com, None, {str(props2)})")

    def test_htmlnode_repr_empty(self):

        node4 = HTMLNode()
        self.assertEqual(repr(node4), f"HTMLNode(None, None, None, None)")

    def test_htmlnode_props_to_html(self):
        props = {"href": "https://test.com"}
        node1 = HTMLNode("a", "Test.com", None, props)
        self.assertEqual(node1.props_to_html(), f' href="https://test.com"')

        props2 = {"href": "https://test.com", "target": "_blank"}
        node2 = HTMLNode("a", "Test.com", None, props2)
        self.assertEqual(
            node2.props_to_html(), f' href="https://test.com" target="_blank"'
        )

    def test_htmlnode_props_to_html_empty(self):
        props3 = {}
        node3 = HTMLNode("a", "Test.com", None, props3)
        self.assertEqual(node3.props_to_html(), None)

        props4 = {}
        node4 = HTMLNode("a", "Test.com", None, props4)
        self.assertEqual(node3.props_to_html(), None)


if __name__ == "__main__":
    unittest.main()
