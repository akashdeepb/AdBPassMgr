from main import main
loop=5
while loop==5:
    print(chr(27)+"[2J")
    print("\n\n\t W e l c o m e   T o  A d B   P a s s w o r d   M a n a g e r  ")
    main()
    c=raw_input("\n\n Do you want to Run Again(y/n) : ")
    if c=='y':
        loop=5
    else:
        loop=0
print("\n\n Shutting down AdBPassMgr ... \n\n\n")
exit()
