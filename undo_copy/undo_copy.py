
import os, shutil

source = "/tmp/test/source" # sys.argv[1]
target = "/tmp/test/target" # sys.argv[2]

files = os.listdir(source) # returns a list of top level directory contents

for file in files:
    to_del = os.path.join(target, file) # join target with source file/directory
    if os.path.isdir(to_del):
        print(f"Removing Directory: {to_del}")
        try:
            shutil.rmtree(to_del) # remove directories and sub-directories
        except FileNotFoundError:
            pass
    else:
        print(f"Removing File: {to_del}")
        try:
            os.remove(to_del) # remove files
        except FileNotFoundError:
            pass

print("Done")