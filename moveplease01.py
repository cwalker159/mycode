#!/usr/bin/env python3

"""A simple script to move two files into ceph_storage/
   Alta3 Research | rzfeeser@alta3.com"""

# standard library imports
import shutil    # shell utilities to move files
import os  # provides access to low level os operations

def main():
    """runtime call"""
    os.chdir('/home/student/mycode/')  #jumps into working directory
    shutil.move('raynor.obj', 'ceph_storage/') # The movers are here! 'raynor.obj' to 'ceph_storage/'

    # prompt user for a new name for file
    xname = input('What is the new name for kerrigan.obj? ') # collect the string from user
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname) # moving kerrigan.obj into
                                                                       # ceph_storage/ with new name

main() # this calls our main function


