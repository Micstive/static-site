from enum import Enum

class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, text_url = None):
        self.text = text
        self.text_type = text_type
        self.text_url = text_url
    
    def __eq__(self, other):
        if (self.text == other.text and 
            self.text_type == other.text_type and
            self.text_url == other.text_url):
            return True
        else:
            return False
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.text_url})"

