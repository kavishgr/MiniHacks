import ebooklib
from ebooklib import epub
import os

for i in os.listdir():
    if i.endswith("epub"):
        book = epub.read_epub(i)
        book = book.get_metadata('DC', 'title')
        contains_title = (book[0])
        book = contains_title[0]
# if book contains kavish hunter then replace
# if not just rename
        book = book.replace(" (for Kavish Gour)", '.epub')	
        print(f"{i} -> {book}")
        os.rename(i, book)

print("DONE")
