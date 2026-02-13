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
    if re.search(r"^(\!){1,6} (.*?)", block) is not None:
        return BlockType.HEADING
    if re.search(r"^```\n[\s\S]*?```$", block) is not None:
        return BlockType.CODE
    if re.search(r"^>.*?", block) is not None:
        return BlockType.QUOTE
    if re.search(r"^(- (.*?)\n)+", block) is not None:
        return BlockType.UNORDERED_LIST
    if re.search(r"^(?:(\d+)\. .*?)+", block) is not None:
        line_numbers = re.findall(r"(\d+)\. ", block)
        increments = True
        for i in range(0, len(line_numbers) - 1):
            if int(line_numbers[i + 1]) - int(line_numbers[i]) == 1  and int(line_numbers[i]) == i + 1:
                continue
            else:
                increments = False
                break
        if increments == True:
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH