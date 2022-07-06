# This program can automatically initialize all the path file, so that you can sure all the path in the whole project are right

import time
import os # Used to get the working path

# -------------------------------------------------------------------------------

# Get working path (so this means 'set_path.py' must be run at the correct working path, and it will effect all the programs path localing)
r_path=os.getcwd()

# A Function that can set a file contain working file info in input path
def SetLoFile(path):
    # read the example file
    with open('./r_path_example.py','r') as f:
        text=f.read()
    
    # get the timestamp and readable time
    timestamp=time.time()
    readable_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    
    # construct the text
    text=text.replace('HERE_IS_R_PATH',r_path)
    text=text.replace('HERE_IS_TIMESTAMP',str(timestamp))
    text=text.replace('HERE_IS_READABLE_TIME',str(readable_time))

    #ready to generate r_path file by using the example
    with open(path+'/r_path.py','w') as f:
        # construct r_path.py file
        f.write(text)

# -----------------------------------------------------------------------------

# Get a iternate path list, ready for set the path_locating file.
path_list=os.walk(r_path)

# provide every single son dir a 'r_path.txt' file
for path,dirs,files in path_list:
    if '.git' in path:
        continue
    SetLoFile(path)


# the SetRPath function is same to run this set_path.py directly
def SetRPath():
    # Get working path (so this means 'set_path.py' must be run at the correct working path, and it will effect all the programs path localing)
    r_path=os.getcwd()

    # Get a iternate path list, ready for set the path_locating file.
    path_list=os.walk(r_path)

    # provide every single son dir a 'r_path.txt' file
    for path,dirs,files in path_list:
        if '.git' in path:
            continue
        SetLoFile(path)

# ---------------------------------------------------------------------------