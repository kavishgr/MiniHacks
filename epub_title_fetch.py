from ebooklib import epub
import os, re

#string to remove from filename
#pattern = re.compile(r"\(for Josianne Machongpi\)")

# if there are multiples patterns
# make a list
todel = "("text_to_remove_from_title")"

for file in os.listdir():
    if file.endswith(".epub") and not file.startswith('.DS_Store'):
        try:
            epubReader = epub.read_epub(file)
            book = epubReader.get_metadata('DC', 'title')
            title = book[0][0]
            if todel in title:
                newtitle = title.replace(todel, "")
                newtitle = newtitle.rstrip(" ")
                newtitle = f"{newtitle}.epub"
                if "/" in newtitle:
                    newtitle = newtitle.replace("/", "-") 
                print(f"Renaming {file} to {newtitle}")
                os.rename(file, newtitle)
            else:
                os.rename(file, title)
        except KeyError:
            continue
        except epub.EpubException as e:
            print(f"Error reading {file}: {e}")
            continue

