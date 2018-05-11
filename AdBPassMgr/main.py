from selection import access, create
from tools import randbld
from encrypt import encrypt
def main():
    print("\n\n\t Select one of the Following ")
    print("\n\n\t 1 - A c c e s s   P a s s w o r d s ")
    print("\n\t 2 - C r e a t e      R a n d o m      P a s s w o r d ")
    print("\n\t 3 - S a v e   P a s s w o r d (w i t h   E n c r y p t i o n) ")
    print("\n\n\t 9 - A d v a n c e   M o d e ")
    print("\n\n\t\t 0 -  E  X  I  T ")
    sel=input("\n Y o u r    S e l e c t i o n  : ")
    if sel==1:
        access()
    elif sel==2:
        randbld()
    elif sel==3:
        print(chr(27)+"[2J")
        print("\n\n\t ---  A d B   P a s s w o r d   M a n a g e r  --- ")
        pwd=raw_input("\n\n Enter Password :  ")
        fname=raw_input("\n\n Enter the file name : ")
        encrypt(fname,pwd)
    elif sel==9:
        print(chr(27)+"[2J")
        print("\n\n ------ A d B P a s s M g r      A d v a n c e   M o d e  -----")
        create()
    elif sel==0:
        print("\n\n Shutting down AdBPassMgr ... ")
        exit()
    else:
        print("\n Invalid Input")

