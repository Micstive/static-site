from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if re.findall(r"^(\!){1,6} (.*?)") is not None:
        return BlockType.HEADING
    if re.findall(r"^`{3}\n(.*?)`{3}") is not None:
        return BlockType.CODE
    if re.findall(r"^>.*?>") is not None:
        return BlockType.QUOTE
    if re.findall(r"^(- (.*?)\n)\1") is not None:
        return BlockType.UNORDERED_LIST
    if re.findall(r"^(\d+ (.*?)\n)+") is not None:
        line_numbers = re.findall(r"^(\d+) .*?\n+")
        increments = True
        for i in range(0, len(line_numbers) - 1):
            if line_numbers[i] >= line_numbers[i + 1]:
                increments = False
                break
        if increments == True:
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH