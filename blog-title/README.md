Converts a blog post title(string) into a URL-friendly format by making it lowercase and replacing spaces with hyphens. And squeeze multiple occurences of hyphens(like `tr -s`).

```shell
➜  ~ blog-title.py "Dummy Blog Post Title"
dummy-blog-post-title

➜  ~ blog-title.py "iptables-- and--- localhost"
iptables-and-localhost
```