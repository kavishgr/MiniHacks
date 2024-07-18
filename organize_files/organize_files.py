import os,shutil

excludes = ['md', 'txt']
pwd = os.getcwd()
dirs = []

for file in os.listdir():
    #e.g ".git"
    if file.startswith('.'):
        continue
 
    if '.' in file:
        filename_ext = file.split('.')
        if filename_ext[1] in excludes:
            continue
        
        # mkdir
        new_dir = filename_ext[0]
        dst = os.path.join(pwd, new_dir)
        if not os.path.exists(dst):
            os.mkdir(dst)
        # move file
        if file.startswith(filename_ext[0]):
            shutil.move(file, dst)
        try:
            readme = os.path.join(dst, "README.md")
            with open(readme, mode='x') as f:
                pass
        except FileExistsError:
            pass


