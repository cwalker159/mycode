#!/usr/bin/env python3

#!/usr/bin/env python3
"""Alta3 Research || Author: CRWalker@carlcodes.com
     Learning about copyiny files and folder"""
# The following line will create the directory if it does not exist already

# import additional code to complete the task    
import shutil
import os

def main():
    """Code to move files around"""
# move into the working directory
os.chdir("/home/student/mycode/")

# copy the fileA to fileB
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

# copy the entire directoryA to directoryB
shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()
