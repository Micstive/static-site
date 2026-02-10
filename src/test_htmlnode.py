import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(
            "p",
            "Random Text",
            None,
            {
            "href": "https://www.google.com",
            "target": "_blank",
        })
        node2 = HTMLNode(
            "p",
            "Random Text",
            None,
            {
            "href": "https://www.google.com",
            "target": "_blank",
        })
        self.assertEqual(node.tag, node2.tag)
        self.assertEqual(node.value, node2.value)
        self.assertEqual(node.children, node2.children)
        self.assertEqual(node.props, node2.props)

    def test_value_only(self):
        node = HTMLNode(
            None,
            "Random Text",
            None,
            None
            )
        node2 = HTMLNode(
            None,
            "Random Text",
            None,
            None
            )
        self.assertEqual(node.tag, node2.tag)
        self.assertEqual(node.value, node2.value)
        self.assertEqual(node.children, node2.children)
        self.assertEqual(node.props, node2.props)

    def test_dif_value(self):
        node = HTMLNode(
            "p",
            "node text",
            None,
            {
            "href": "https://www.google.com",
            "target": "_blank",
        })
        node2 = HTMLNode(
            "p",
            "node2 text",
            [HTMLNode(), HTMLNode()],
            {
            "href": "https://www.google.com",
            "target": "_blank",
        })
        self.assertEqual(node.tag, node2.tag)
        self.assertNotEqual(node.value, node2.value)
        self.assertNotEqual(node.children, node2.children)
        self.assertEqual(node.props, node2.props)    
        
    def test_null_args_except_value(self):    
        node = HTMLNode(value="only value is given")
        node2 = HTMLNode(value="only value is given")
        self.assertEqual(node.tag, node2.tag)
        self.assertEqual(node.value, node2.value)
        self.assertEqual(node.children, node2.children)
        self.assertEqual(node.props, node2.props)

    def test_dif_order_dict(self):
        node = HTMLNode(
            "p",
            "Random Text",
            None,
            {
            "href": "https://www.google.com",
            "target": "_blank",
        })
        node2 = HTMLNode(
            "p",
            "Random Text",
            None,
            {
            "target": "_blank",
            "href": "https://www.google.com",      
        })
        self.assertEqual(node.tag, node2.tag)
        self.assertEqual(node.value, node2.value)
        self.assertEqual(node.children, node2.children)
        self.assertEqual(node.props, node2.props)

    def test_props_to_html(self):
        node = HTMLNode(
            "p",
            "Random Text",
            None,
            {
            "href": "https://www.google.com",
            "target": "_blank",
        })
        node2 = HTMLNode(
            "p",
            "Random Text",
            None,
            {}
            )
        assert node.props_to_html() == " href=\"https://www.google.com\" target=\"_blank\""
        assert node2.props_to_html() == ""

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!", {
                "href": "https://www.google.com",
                "target": "_blank",
            })
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\" target=\"_blank\">Hello, world!</a>")


    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_grandchildren(self):
        grandchild_node1 = LeafNode("b", "grandchild1")
        grandchild_node2 = LeafNode("i", "grandchild2")
        grandchild_node3 = LeafNode("a", "grandchild3", {
                    "href": "https://www.google.com",
                    "target": "_blank",
                })

        child_node = ParentNode("span", [grandchild_node1, grandchild_node2, grandchild_node3])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild1</b><i>grandchild2</i><a href=\"https://www.google.com\" target=\"_blank\">grandchild3</a></span></div>",
        )


if __name__ == "__main__":
    unittest.main()