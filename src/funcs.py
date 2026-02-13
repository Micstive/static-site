import re
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

def extract_markdown_images(text):
    image_list = []
    alt_images = re.findall(r"!\[(.*?)\]\(https://.*?\..*?/.*?\..*?\)", text)
    images = re.findall(r"!\[.*?\]\((https://.*?\..*?/.*?\..*?)\)", text)
    if len(alt_images) != len(images):
        raise Exception("number of alt text does not equal number of images")
    for i in range(0, len(images)):
        image_list.append((alt_images[i], images[i]))
    return image_list


def extract_markdown_links(text):
    links_list = []
    alt_texts = re.findall(r"(?<!\!)\[(.*?)\]\(https://.*?\..*?\)", text)
    links = re.findall(r"(?<!\!)\[.*?\]\((https://.*?\..*?)\)", text)
    if len(alt_texts) != len(links):
        raise Exception("number of anchor text does not equal number of links")
    for i in range(0, len(links)):
        links_list.append((alt_texts[i], links[i]))
    return links_list

def split_nodes_image(old_nodes):
    nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes.append(node)
            continue
        if node.text == "":
            nodes.append(node)
            continue
        images_info = extract_markdown_images(node.text)
        original_text = node.text
        for image_info in images_info:
            split_text = original_text.split(f"![{image_info[0]}]({image_info[1]})", 1)
            first_section = split_text[0]
            original_text = split_text[1]
            nodes.append(TextNode(first_section, TextType.TEXT))
            nodes.append(TextNode(image_info[0], TextType.IMAGE, image_info[1]))
        if original_text != "" and original_text is not None:
            nodes.append(TextNode(original_text, TextType.TEXT))
    return nodes

def split_nodes_link(old_nodes):
    nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes.append(node)
            continue
        if node.text == "":
            nodes.append(node)
            continue
        links_info = extract_markdown_links(node.text)
        original_text = node.text
        for link_info in links_info:
            first_section, original_text = original_text.split(f"[{link_info[0]}]({link_info[1]})", 1)
            nodes.append(TextNode(first_section, TextType.TEXT))
            nodes.append(TextNode(link_info[0], TextType.LINK, link_info[1]))
        if original_text != "" and original_text is not None:
            nodes.append(TextNode(original_text, TextType.TEXT))
    return nodes

def text_to_textnodes(text):
    textnodes = []
    textnodes.extend(split_nodes_image(split_nodes_link(split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter([TextNode(text, TextType.TEXT)], "**", TextType.BOLD), "_", TextType.ITALIC), "`", TextType.CODE))))
    
    #for section in split_nodes_image([TextNode(text, TextType.TEXT)]):
     #   for piece in split_nodes_link([section]):
      #      for a in split_nodes_delimiter([piece], "`", TextType.CODE):
       #         textnodes.append(a)
    return textnodes

def markdown_to_blocks(markdown):
    block_list = []
    for block in markdown.split("\n\n"):
        if re.findall(r".", block) is not None:
            block_list.append(block.strip())
    return block_list