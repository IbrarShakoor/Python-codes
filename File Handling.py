#file handling:



f=open('readfile.txt','r')
print("\t\tRedaing the whole file")
# print(f.read())#it will read the whole file

#in order to check the option which option or build in function do we have press
#cntrl+space


print()
print("\t\tReading the first line ")
print(f.readline())  #single line
print(f.readline(),end="")#single line
print(f.__next__(),end="")#single line


print()
print("\t\tReading the first line ")
print(f.readline(5))  #Number of charcters you wanna print



