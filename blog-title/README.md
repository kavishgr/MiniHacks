Converts a blog post title(string) into a URL-friendly format by making it lowercase and replacing spaces with hyphens. And squeeze multiple occurences of hyphens(like `tr -s`).

```shell
➜  ~ echo "Dummy Blog Post Title" | blog-title.py 
dummy-blog-post-title

➜  ~ echo "iptables-- and--- localhost" | blog-title.py 
iptables-and-localhost
```

Bash implementation - `blog-title.sh`