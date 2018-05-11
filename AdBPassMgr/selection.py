import os
from tools import specmenu
from decrypt import decrypt
def access():
    print(chr(27)+"[2J")
    print("\n\n\t A d B   P a s s w o r d   M a n a g e r")
    print("\n\n\t Encrypted Files Found : ")
    dir_path=os.path.dirname(os.path.realpath(__file__))
    for file in os.listdir(dir_path):
        if file.endswith(".bin"):
            print("\t\t--> " +file)
    fname=raw_input("\n Enter the File Name : ")
    decrypt(fname)

def create():
    print(chr(27)+"[2J")
    print("\n\n\t A d B   P a s s w o r d   M a n a g e r ")
    print("\n +++++     A d v a n c e     M o d e     +++++ ")
    specmenu()
