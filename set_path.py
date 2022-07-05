# This program can automatically initialize all the path file, so that you can sure all the path in the whole project are right

import time
import os # Used to get the working path

# Get working path (so this means 'set_path.py' must be run at the correct working path, and it will effect all the programs path localing)
r_path=os.getcwd()

path_list=os.walk(r_path)

for a,b,c in path_list:
    if '.git' in a:
        continue
    print(a,b,c)

print(path_list)