# This program can automatically initialize all the path file, so that you can sure all the path in the whole project are right

import time
import os # Used to get the working path



# Get working path (so this means 'set_path.py' must be run at the correct working path, and it will effect all the programs path localing)
r_path=os.getcwd()

# A Function that can set a file contain working file info in input path
def SetLoFile(path):
    with open(path+'/r_path.txt','w') as f:
        f.write(r_path)




# Get a iternate path list, ready for set the path_locating file.
path_list=os.walk(r_path)

# provide every single son dir a 'r_path.txt' file
for path,dirs,files in path_list:
    if '.git' in path:
        continue
    SetLoFile(path)