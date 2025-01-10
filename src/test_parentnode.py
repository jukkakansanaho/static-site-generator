import unittest

from leafnode import LeafNode
from parentnode import ParentNode

ln1 = LeafNode(None, "Normal text")
ln2 = LeafNode("b", "Bold text")
ln3 = LeafNode("i", "Italic text")
ln4 = LeafNode("a", "Link text", None, {"href": "https://test.com", "target": "_blank"})
ln5 = LeafNode("li", "List item")
ln6 = LeafNode("blockquote", "This is a quote")
ln7 = LeafNode("code", "print(f'This is code')")
ln8 = LeafNode(
    "img", "Image", None, {"src": "url/of/image.jpg", "alt": "Description of image"}
)
ln9 = LeafNode("th", "Table header")
ln10 = LeafNode("td", "Table data")

tc1 = (
    ParentNode("p", [ln2, ln1, ln3, ln1]),
    "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>",
)

tc2 = (
    ParentNode("h2", [ln1, ln2, ln1]),
    "<h2>Normal text<b>Bold text</b>Normal text</h2>",
)

tc3 = (
    ParentNode("ul", [ln5, ln5, ln5]),
    "<ul><li>List item</li><li>List item</li><li>List item</li></ul>",
)
tc4 = (
    ParentNode("ol", [ln5, ln5, ln5]),
    "<ol><li>List item</li><li>List item</li><li>List item</li></ol>",
)
tc5 = (ParentNode("p", [ln6]), "<p><blockquote>This is a quote</blockquote></p>")
tc6 = (ParentNode("p", [ln7]), "<p><code>print(f'This is code')</code></p>")
tc7 = (
    ParentNode(
        "table",
        [ParentNode("tr", [ln9, ln9, ln9]), ParentNode("tr", [ln10, ln10, ln10])],
    ),
    "<table><tr><th>Table header</th><th>Table header</th><th>Table header</th></tr><tr><td>Table data</td><td>Table data</td><td>Table data</td></tr></table>",
)
tc8 = (
    ParentNode(
        "ol",
        [
            ParentNode("li", [ParentNode("p", [ln2, ln1, ln3, ln1])]),
            ParentNode("li", [ParentNode("p", [ln2, ln1, ln3, ln1])]),
            ParentNode("li", [ParentNode("p", [ln2, ln1, ln3, ln1])]),
        ],
    ),
    "<ol><li><p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p></li><li><p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p></li><li><p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p></li></ol>",
)

dataset1 = [tc1]
dataset2 = [tc2]
dataset3 = [tc3, tc4]
dataset4 = [tc5]
dataset5 = [tc6]
dataset6 = [tc7]
dataset7 = [tc8]


class TestParentNode(unittest.TestCase):

    def test_parentnode_to_html_basic(self):
        node1 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text 1"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text 2"),
            ],
        )
        self.assertEqual(
            node1.to_html(),
            f"<p><b>Bold text</b>Normal text 1<i>Italic text</i>Normal text 2</p>",
        )

    def test_parentnode_to_html_empty_children(self):
        try:
            pn = ParentNode("p", [])
        except TypeError as e:
            self.assertEqual(type(e), TypeError)
        else:
            self.fail("TypeError not raised")

    def test_parentnode_to_html_b_and_i(self):
        testcases = dataset1
        for testcase in testcases:
            # print(f"\n---- testcase: \ninput: {testcase[0]} \nexpected: {testcase[1]}")
            self.assertEqual(testcase[0].to_html(), testcase[1])

    def test_parentnode_to_html_h2_b_i(self):
        testcases = dataset2
        for testcase in testcases:
            # print(f"\n---- testcase: \ninput: {testcase[0]} \nexpected: {testcase[1]}")
            self.assertEqual(testcase[0].to_html(), testcase[1])

    def test_parentnode_to_html_ul_and_ol(self):
        testcases = dataset3
        for testcase in testcases:
            # print(f"\n---- testcase: \ninput: {testcase[0]} \nexpected: {testcase[1]}")
            self.assertEqual(testcase[0].to_html(), testcase[1])

    def test_parentnode_to_html_blockquote(self):
        testcases = dataset4
        for testcase in testcases:
            # print(f"\n---- testcase: \ninput: {testcase[0]} \nexpected: {testcase[1]}")
            self.assertEqual(testcase[0].to_html(), testcase[1])

    def test_parentnode_to_html_code(self):
        testcases = dataset5
        for testcase in testcases:
            # print(f"\n---- testcase: \ninput: {testcase[0]} \nexpected: {testcase[1]}")
            self.assertEqual(testcase[0].to_html(), testcase[1])

    def test_parentnode_to_html_table(self):
        testcases = dataset6
        for testcase in testcases:
            # print(f"\n---- testcase: \ninput: {testcase[0]} \nexpected: {testcase[1]}")
            self.assertEqual(testcase[0].to_html(), testcase[1])

    def test_parentnode_to_html_ol_with_parents(self):
        testcases = dataset7
        for testcase in testcases:
            # print(f"\n---- testcase: \ninput: {testcase[0]} \nexpected: {testcase[1]}")
            self.assertEqual(testcase[0].to_html(), testcase[1])

    def test_parentnode_repr(self):
        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text 1"),
            LeafNode("i", "Italic text"),
            LeafNode(None, "Normal text 2"),
        ]

        node1 = ParentNode("p", children)
        self.assertEqual(repr(node1), f"ParentNode(p, children: {str(children)}, None)")
