Move your `jekyll` blog post file from the `_drafts/` folder to the `_posts/` folder. There should only be one post in the drafts folder. The script will rename it by prefixing today's date in the file name, commits it to git, and get a desktop notification when the URL is active.

Only works on macos. On linux, you need to call `inotify`.

```shell
python3 JekyllGitPages.py
```
