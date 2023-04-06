# Use with caution

- [JekyllGitPages.py](https://github.com/kavishgr/MiniHacks/blob/master/JekyllGitPages.py) - Move your blog post from the _drafts/ folder to _posts/, rename it, commits it to git, and get a desktop notification when the URL is active.

- [mem_usage.py](https://github.com/kavishgr/MiniHacks/blob/master/mem_usage.py) - Print the system's memory usage, and if memory usage increased to 90% or higher, print a warning. Can be executed as ad-hoc command for Ansible tasks. (Just for fun.)

- [NagiosInstall.py](https://github.com/kavishgr/MiniHacks/blob/master/NagiosInstall.py) - Nagios Core automated installation on CentOS 7.

- [hostbyname.py](https://github.com/kavishgr/MiniHacks/blob/master/hostbyname.py) - Iterate over a list of domains to find its IP addresses from a file. **Usage:** python3 hostbyname.py [file]

- [undo_copy.py](https://github.com/kavishgr/MiniHacks/blob/master/undo_copy.py) - Reverse the action of `cp` in Python.

- [undo_copy.go](https://github.com/kavishgr/MiniHacks/blob/master/undo_copy.go) - Reverse the action of `cp` in Go.

- [zipcomic.py](https://github.com/kavishgr/MiniHacks/blob/master/zipcomic.py) - Comic Book downloader for **zipcomic.com** (`-r` for range)

```shell
python3 zipcomic.py -u "https://www.zipcomic.com/a-lucky-luke-adventure"
python3 zipcomic.py -u "https://www.zipcomic.com/a-lucky-luke-adventure" -r 3:8
```

- [zipcomic.go](https://github.com/kavishgr/ZipComic-Downloader) - The Go version.

- [artsydl.go](https://github.com/kavishgr/MiniHacks/blob/master/artsydl.go)  - Download all jpegs for an entire album. The excessive use of hashmaps and channels could potentially complicate future changes. However, it currently functions as intended.

```shell
artsydl.go "https://www.artsy.net/show/danziger-gallery-tod-papageorge-on-the-acropolis"
```

- [artsydl.py](https://github.com/kavishgr/MiniHacks/blob/master/artsydl.py) (depends on `wget`)

```shell
python3 artsydl.py "https://www.artsy.net/show/danziger-gallery-tod-papageorge-on-the-acropolis"
```


