from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes.append(node)
            continue
        if node.text.count(delimiter) % 2 == 1:
            raise Exception("missing matching tag")
        count = 0
        for section in node.text.split(delimiter):
            if count % 2 == 0:
                nodes.append(TextNode(section, TextType.TEXT))
            else:
                nodes.append(TextNode(section, text_type))
            count += 1
    return nodes
        