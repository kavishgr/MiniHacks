Scrape an entire album on `artsy.net` and download all the jpegs. Was just learning. The excessive use of hashmaps and channels could potentially complicate future changes. However, I'm not sure if it still works. Implemented in both `go` and `python`.

### Usage

```shell
# e.g
go run artsydl.go "https://www.artsy.net/show/danziger-gallery-tod-papageorge-on-the-acropolis"

python3 artsydl.py "https://artsy.net/......"
```

The `go` script requires:

- "github.com/anaskhan96/soup"
- "github.com/schollz/progressbar"

The `python` script requires:

- BeautifulSoup
- requests
- wget(cli tool)