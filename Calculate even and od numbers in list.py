from array import *

list=[1,2,3,54,5,7,8,44]


def even_odd(list):
    c1=0
    c2=0
    for i in list:
        if(i%2==0):
            c1+=1
        else:
            c2+=1
    return c1,c2

e,odd=even_odd(list)
print("Even Numbers:",e)
print("Odd Numbers:",odd)


print("Odd Numbers:{}  Even Nubers:{} ".format(odd,e))#for beautiful format


#Calculate the names which has length smaller than 5
print()
def count(lst):
    c1 = 0
    c2 = 0
    for i in lst:
      if(len(i)>=5):
        c1+=1
      else:
        c2+=1

    return c1,c2
x=int(input("How many names:"))
i=0
lst=[]
while(i<x):
   y=input("Enter the names:")
   lst.append(y)
   i+=1

l,g=count(lst)

print("Greater Name:{}  Less name:{}".format(g,l))

print(lst)
