
#How to read from one file and copy that data to another file

f=open('readfile.txt','r')

f1=open('Writingfile','w')

for data in f:
    #print(data,end="")It will print all of teh lines on console
    f1.write(data)#it will copy everything from readfile to Writingfile
