import string
import random
from encrypt import encrypt
def difbld():
    alf=string.ascii_letters
    dig=string.digits
    spl='$'+'_'+'%'+'&'+'*'
    nc=input("\n Number of Alphabets  : ")
    ns=input("\n Number of Special Ch : ")
    nd=input("\n Number of Digits     : ")
    print("\n\n Select the format ")
    print("\n 1 > alphabets - special_characters - digits ")
    print("\n 2 > alphabets -      digits        - special characters ")
    print("\n 3 > special c -     alphabets      - digits ")
    print("\n 4 > special c -      digits        - alphabets ")
    print("\n 5 > digits    - special characters - alphabets ")
    print("\n 6 > digits    -     alphabets      - special characters ")
    com=input("\n\n\t S E L E C T I O N : ")
    loop=3
    while loop==3:
        fal=''.join(random.choice(alf) for i in range(nc))
        fdg=''.join(random.choice(dig) for i in range(nd))
        fsp=''.join(random.choice(spl) for i in range(ns))
        if com==1:
            pwd=fal+fsp+fdg
        elif com==2:
            pwd=fal+fdg+fsp
        elif com==3:
            pwd=fsp+fal+fdg
        elif com==4:
            pwd=fsp+fdg+fal
        elif com==5:
            pwd=fdg+fsp+fal
        elif com==6:
            pwd=fdg+fal+fsp
        else:
            print("\n\n Invalid Selection")
        print(chr(27)+"[2J")
        print("\n\n\t ---  A d B   P a s s w o r d   M a n a g e r  --- ")
        print("\n - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        print("\n\n G e n e r a t e d     P a s s w o r d   : " + pwd)
        print("\n - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        print("\n\n 1 - Generate New Password ")
        print("\n 2 - Save this Password (with Encryption ) ")
        print("\n\t 0 (or any other key) - Continue... ")
        sel=input("\n S E L E C T I O N : ")
        if sel==1:
            loop=3
        elif sel==2:
            fname=raw_input("\n\n Enter File Name : ")
            encrypt(fname,pwd)
        else:
            loop=0
def numbld():
    num=input("\n\n Enter the number of Characters : ")
    chars=string.ascii_letters+string.digits
    loop=2
    while loop==2:
        print(chr(27)+"[2J")
        print("\n\n\t ---  A d B    P a s s w o r d   M a n a g e r  --- ")
        print("\n - - - - - - - - - - - - - - - - - - - - - - - ")
        pwd=''.join(random.choice(chars) for i in range(num))
        print("\n\n[[[ Generated Password  :  "+pwd+"        ]]]")
        print("\n - - - - - - - - - - - - - - - - - - - - - - - ")
        print("\n\n 1 - Generate New Password ")
        print("\n\n 2 - Save this Password (with Encryption) ")
        print("\n\n\t 0 (or any other key) - Continue... ")
        sel=input("\n\n\t S e l e c t i o n : ")
        if sel==1:
            loop=2
        elif sel==2:
            fname=raw_input("\n Enter File Name : ")
            encrypt(fname,pwd)
            loop=0
        else:
            loop=0
def keybld():
    print("\n\n\t -------  K E Y W O R D    P A S S W O R D   B U I L D E R ---- ")
    key=raw_input("\n\n Enter the KEYWORD : ")
    size=input("\n\n Enter the No. of additional chars reqd (excluding key)  : ")
    chars=string.ascii_letters+string.digits+'$'+'_'+'%'+'&'+'*'
    loop=5
    while loop==5:
        print(chr(27)+"[2J")
        print("\n\n\t ---  A d B   P a s s w o r d   M a n a g e r  --- ")
        pwd=''.join(random.choice(chars) for i in range(size))
        print("\n - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        passw=key+pwd
        print("\n\n G e n e r a t e d   P  a s s w o r d :  "  + passw)
        print("\n - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        print("\n\n 1 - Generate new password ")
        print("\n 2 - Save this Password (with Encryption) ")
        print("\n\n\t 0 (or Any other key) - Continue... ")
        c=input("\n\t S e l e c t i o n :  ")
        if c==1:
            loop=5
        elif c==2:
            fname=raw_input("\n\n Enter the Filename : ")
            encrypt(fname,passw)
            loop=0
        else:
            loop=0
