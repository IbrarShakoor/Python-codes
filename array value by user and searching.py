
from array import *
array=array('i',[])#creating the empty array

n=int(input("Enter the length of array:"))
print("Enter values:")
for i in range(n):
    x=int(input()) #asking values
    array.append(x) #appending at the end

print(array)





y=int(input("Enter the search value:"))

#searching by build in fun;;
print("index is=",array.index(y))


print("Manually:")
found=0
print()
for i in range(n):
    if(y==array[i]):
        found=1
        print("found and the value is=",y)
if(found==0):
    print("not found")



