import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_dif_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("1234", TextType.BOLD)
        self.assertNotEqual(node, node2)    
        
    def test_dif_TextType(self):    
        node = TextNode("This is a text node", TextType.PLAIN, "someurl")
        node2 = TextNode("This is a text node", TextType.LINK, "someurl")
        self.assertNotEqual(node, node2)

    def test_url_is_none(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node2) 


if __name__ == "__main__":
    unittest.main()