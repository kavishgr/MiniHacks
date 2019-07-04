# Author      : Kavish Gour
#
# Email       : kavishgr@protonmail.com // kavishgour1@gmail.com
#
# Inspired by : https://dev.to/_andy_lu_/python-for-bash-3798
#
# Description : JekyllGitPages.py => move your blog post from the _drafts/ folder to _posts/, rename it,
#               commits it to git, and get a desktop notification when the URL is active.
#
# Usage       : Drop your 'file.md' in _drafts/ and run the script in the background.
#               


#######################################################################################################
#                                         IMPORTS                                                     #
#######################################################################################################

import subprocess as sp
from datetime import date
import requests
import time
import os

## Replace path 

newPost = sp.getoutput("ls /Users/kavish/Documents/GitHub/kavishgr.github.io/_drafts/").split("\n")
today = date.today()
blogPostDate = f"{today.year}-{today:%m}-{today:%d}" # Jekyll date formatting: YYYY-MM-DD
myBlog = "/Users/kavish/Documents/GitHub/kavishgr.github.io/" 

#######################################################################################################
#                                         FUNCTIONS                                                   #
#######################################################################################################

def moveToPosts():
    global newPost
    global blogPostDate

    postInDrafts = len(newPost)

    if (postInDrafts == 1):
        srcPath = "/Users/kavish/Documents/GitHub/kavishgr.github.io/_drafts/" + newPost[0]
        destPath = "/Users/kavish/Documents/GitHub/kavishgr.github.io/_posts/" + blogPostDate + "-" + newPost[0]

        sp.run(f"mv {srcPath} {destPath}", shell=True)

        return [destPath, newPost[0]] ## Arguments for runGit() in "__main__".

    elif (postInDrafts == 0):
        print("Drafts folder is empty")
        print("Exiting")
        raise SystemExit

    else:
        print("There's more than 1 post!!")
        print("Exiting")
        raise SystemExit

def runGit(fullPath, newPost):

    global myBlog

    commitMsg = "'Testing'"
    os.chdir(myBlog)
    c1 = "git add " + fullPath
    c2 = "git commit -m " + commitMsg
    c3 = "git push"

    commands = [c1, c2, c3]

    for cmd in commands:
        run = sp.run(cmd, shell=True) 

def postStatus():
    global newPost
    global today
    urlDate = f"{today.year}/{today:%m}/{today:%d}/"
    # Replace URL
    blogPostUrl = f'https://kavishgr.github.io/articles/' + urlDate + str(newPost.strip('.md')) + '.html'

    time.sleep(60)
    response = requests.get(blogPostUrl)
    statusCode = response.status_code

    if statusCode == 200:

        ## On Linux, use 'inotify'.

        sp.run('osascript -e \'display notification "Blog post is up" with title "gitpages.py" subtitle "Status code: 200" sound name "Submarine"\'', shell=True)
    
    else:

        sp.run(f'osascript -e \'display notification "Failed!!" with title "gitpages.py" subtitle "Status code: {statusCode}" sound name "Submarine"\'', shell=True)

#######################################################################################################
#                                         MAIN                                                        #
#######################################################################################################

if __name__ == "__main__":
    pathToPost, newPost = moveToPosts()
    runGit(pathToPost, newPost)
    postStatus()
