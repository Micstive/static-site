import unittest

from textnode import TextNode, TextType
from funcs import split_nodes_delimiter

class TestFuncs(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ])

    def test_not_text(self):
        node = TextNode("This is text with a `code block` word", TextType.CODE)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
                TextNode("This is text with a `code block` word", TextType.CODE)
            ])

    def test_multiple(self):
        node1 = TextNode("This is text with a `Node1` word", TextType.TEXT)
        node2 = TextNode("This is text with a `Node2` word", TextType.TEXT)
        node3 = TextNode("This is text with a `Node3` word", TextType.TEXT)
        node4 = TextNode("This is text with a `Node4` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2, node3, node4], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("Node1", TextType.CODE),
                TextNode(" word", TextType.TEXT),
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("Node2", TextType.CODE),
                TextNode(" word", TextType.TEXT),
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("Node3", TextType.CODE),
                TextNode(" word", TextType.TEXT),
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("Node4", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ])
        
    def test_bold(self):
        node = TextNode("This is text with a **bolded words** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded words", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ])
    def test_empty_text(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
                TextNode("", TextType.TEXT),
            ])






if __name__ == "__main__":
    unittest.main()