import string
import random
import Tkinter as tk
from builder import numbld,difbld,keybld
from encrypt import encrypt
def randbld():
    size=8
    chars=string.ascii_letters+string.digits
    loop=1
    while loop==1:
        print(chr(27)+"[2J")
        print("\n\n\t ---  A d B   P a s s w o r d   M a n a g e r  --- ")
        print("\n --  R a n d o m   P a s s    B u i l d e r --")
        print("\n -------------------------------------------------")
        pwd=''.join(random.choice(chars) for i in range(size))
        print("\n\n\t[[[ Generated Password : "+pwd+"          ]]]")
        print("\n\n ------------------------------------------------")
        print("\n\t 1 - Generate New Random Password ")
        print("\n\t 2 - Save this password (With Encryption)")
        print("\n\t 3 - copy to clipboard and save (With encryption)")
        print("\n\t\t 0 (or any other) - To Continue... ")
        sel=input("\n\n Enter your Selection : ")
        if sel==1:
            loop=1
        elif sel==2:
            fname=raw_input("\n\n Enter File Name : ")
            encrypt(fname,pwd)
            loop=0
        elif sel==3:
            copyclip(pwd)
            fname=raw_input("\n\n Enter File Name : ")
            encrypt(fname,pwd)
            loop=0
        else:
            loop=0
	      
	     
            

def specmenu():
    print("\n\n\n Create Password Based on - ")
    print("\n\t 1 - Number of Characters ")
    print("\n\t 2 - Different Chars ")
    print("\n\t 3 - Using Keywords (less secure)")
    sel=input("\n\n\t Enter your selection : ")
    if sel==1:
        numbld()
    elif sel==2:
        difbld()
    elif sel==3:
        keybld()
    else:
        print("\n\n Invalid selection ")

def copyclip(pwd):
	cb = tk.Tk()
	cb.withdraw()
	cb.clipboard_clear()
	cb.clipboard_append(pwd)
	cb.after(100000,lambda:cb.distroy())
	cb.mainloop()
	print("\n copied to clipboard")


