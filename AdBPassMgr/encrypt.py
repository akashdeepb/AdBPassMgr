import os
def encrypt(fname,pwd):
    name=fname+".bin"
    if os.path.isfile(name):
        print("\n\n File Already Exists ")
        sel=raw_input("\n Do you want to over-write?(y/n) : ")
        if sel=='y' or sel == 'Y':
            stat=1
        else:
            stat=0
    else:
        stat=1
    if stat==1:
        data=''
        pin=raw_input("\n\n Enter PIN : ")
        off=ord(pin[0])
        off=off/2
        of2=ord(pin[3])
        of2=of2/2
        file=open(fname+".bin",'w')
        for i in range(0,len(pwd)):
            if i%2==0:
                data=data+chr(ord(pwd[i])-off)
            else:
                data=data+chr(ord(pwd[i])+of2)
        file.write(data)
        file.close()
        print("\n\n --- E n c r y p t i o n     C o m p l e t e --- ")
    else:
        print("\n\n --- E n c r y p t i o n     F a i l e d --- ")
