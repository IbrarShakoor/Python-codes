f=open('Ibrar.jpg','rb')#image are in binary so read binary =rb
f1=open('copiedfile.jpg','wb')

for i in f:
    # print(i)  #it will print all of the data of picture in to binary
    f1.write(i)#it will write picture means copy our picture to another file
