import os
def decrypt(fname):
    pwd=''
    print("\n\n D e c r y p t i n g  : " + fname)
    if os.path.isfile(fname):
        file= open(fname,"r")
        pin=raw_input("\n\n Enter    P I N  : ")
        off=ord(pin[0])
        off=off/2
        of2=ord(pin[3])
        of2=of2/2
        data=file.read()
        for i in range(0, len(data)):
            if i%2==0:
                pwd=pwd+chr(ord(data[i])+off)
            else:
                pwd=pwd+chr(ord(data[i])-of2)
        print("\n - - - - - - - - - - - - - - - - - - - - - - - - ")
        print("\n\nD e c r y p t e d    P a s s w o r d  : " + pwd)
        print("\n - - - - - - - - - - - - - - - - - - - - - - - - ")
    else:
        print("\n\n- - No Match Found  - - " )
