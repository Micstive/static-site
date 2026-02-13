import unittest

from textnode import TextNode, TextType
from funcs import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes, markdown_to_blocks
from blocktype import BlockType, block_to_block_type

class TestFuncs(unittest.TestCase):
    def test_block_to_blocktype_headings(self):
            md = """
!!!!!! This has !!!!!! paragraph

!!!!! This has !!!!! paragraph

!!!! This has !!!! paragraph

!!! This has !!! paragraph

!! This has !! paragraph

! This has ! paragraph
"""
            blocks = markdown_to_blocks(md)
            block_types = []
            for block in blocks:
                block_types.append(block_to_block_type(block))
            self.assertListEqual(
                block_types,
                [
                    BlockType.HEADING,
                    BlockType.HEADING,
                    BlockType.HEADING,
                    BlockType.HEADING,
                    BlockType.HEADING,
                    BlockType.HEADING,

                ],
            )
    
    def test_block_to_blocktype_code(self):
            md = """
```
This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line```

```
This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line```
```

```This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line```
"""
            blocks = markdown_to_blocks(md)
            block_types = []
            for block in blocks:
                block_types.append(block_to_block_type(block))
            self.assertListEqual(
                block_types,
                [
                    BlockType.CODE,
                    BlockType.CODE,
                    BlockType.PARAGRAPH,
                ],
            )


    def test_block_to_blocktype_quote(self):
            md = """
>quotations we will see >

> another quote

>a third quote
"""
            blocks = markdown_to_blocks(md)
            block_types = []
            for block in blocks:
                block_types.append(block_to_block_type(block))
            self.assertListEqual(
                block_types,
                [
                    BlockType.QUOTE,
                    BlockType.QUOTE,
                    BlockType.QUOTE,
                ],
            )

    def test_block_to_blocktype_unordered_list(self):
            md = """
- this a unordered list
- second item
- third item

- another unordered list
- second item of the seoncd list

-this should be a paragraph
- this should still be a paragraph
"""
            blocks = markdown_to_blocks(md)
            block_types = []
            for block in blocks:
                block_types.append(block_to_block_type(block))
            self.assertListEqual(
                block_types,
                [
                    BlockType.UNORDERED_LIST,
                    BlockType.UNORDERED_LIST,
                    BlockType.PARAGRAPH,
                ],
            )


    def test_block_to_blocktype_ordered_lists(self):
            md = """
1. ordered list

1. this a ordered list
2. second item
3. third item

1. another ordered list
2. second item of the second list

1.this should be a paragraph
2. this should still be a paragraph

2. this should be a parag
3. this should be a parag

1. this should be a para
2. this should be a para
4. still

1. ord
2. ord
3. ord4.
4. ord1.
5. d
6. a
7. 
8. havppy
"""
            blocks = markdown_to_blocks(md)
            block_types = []
            for block in blocks:
                block_types.append(block_to_block_type(block))
            self.assertListEqual(
                block_types,
                [
                    BlockType.ORDERED_LIST,
                    BlockType.ORDERED_LIST,
                    BlockType.ORDERED_LIST,
                    BlockType.PARAGRAPH,
                    BlockType.PARAGRAPH,
                    BlockType.PARAGRAPH,
                    BlockType.ORDERED_LIST,
                ],
            )


    def test_block_to_blocktype_all(self):
            md = """
This should be a paragraph


!!!!! This has !!!!! paragraph

```
This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line```

>quotations we will see >

- this a unordered list
- second item
- third item

1. ord
2. ord
3. ord4.
4. ord1.
5. d
6. a
7. 
8. havppy
"""

            blocks = markdown_to_blocks(md)
            block_types = []
            for block in blocks:
                block_types.append(block_to_block_type(block))
            self.assertListEqual(
                block_types,
                [
                    BlockType.PARAGRAPH,
                    BlockType.HEADING,
                    BlockType.CODE,
                    BlockType.QUOTE,
                    BlockType.UNORDERED_LIST,
                    BlockType.ORDERED_LIST,
                ],
            )

if __name__ == "__main__":
    unittest.main()