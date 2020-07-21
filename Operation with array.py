
from numpy import *
num=array([1,2,34,5,6])
#how can we add 5 in each value:

for i in range(len(num)):
    num[i]=num[i]+5;
    print(num[i])

#anotehrt solution:
num1=num+5
print(num1)

print()


#How to add two arrays:
array3=num+num1
print(array3)


#hopw to find the sin,cos,tan and othet geomrtric operation:
num2=array([1,2,34,5,6])
print(sum(num2))
print(min(num2))
print(max(num2))
print(sort(num2))




print(sin(num2))
print(sin(num2))
print(cos(num2))
print(log(num2))
print(sqrt(num2))

num3=array([1,3,54,6,5])
num4=array([1,3,54,6,5])
#Concatenate arrays:
print(concatenate([num3,num4]))
print()

#how to copy 1 array into brand new array:
array=array([1,3,5,6])
arr=array#after coping the value in to arr both arrays are at the same address
print(id(array))
print(id(arr))


print()
print("Shallow copy")
#if you want to change the address after coping two methods shallow copy :

arr=array.view() #after coping the value in to arr both arrays are at the diff address
arr[1]=18838
print(arr)
print(array)
print(id(array))
print(id(arr))

print()
print("Deep copy")
#The 2nd method is Deep copy:in this copy the array dont depends upon each other
#means by changing one value of any array wont effect other array,but it does inb shallow
#copy

arr=array.copy() #after coping the value in to arr both arrays are at the diff address and does not depend on each other

arr[1]=2000
print(arr)
print(array)
print(id(array))
print(id(arr))

#Quize Question:
from numpy import *
arr1 = array([1,2,3,4,5])
arr2 = array([5,6,7,8,9])
arr3 = array([])
for i in range(5):
      arr1[i]= arr1[i]+arr2[i]
arr3=arr1
print(arr3)

print()
arr = array([1, 2, 43, 5])
brr = array([2, 4, 6])

for i in range(len(brr)):
            arr[i]=arr[i]+brr[i]
print(arr)


print()
arr = array([1, 2, 43, 5])
for i in range(len(arr)-1):
    if(arr[0]<arr[i+1]):
        temp=arr[0]
        arr[0]=arr[i+1]
        arr[i + 1]=temp

print("max=",arr[0])

for i in range(len(arr)-1):
    if(arr[0]>arr[i+1]):
        temp=arr[0]
        arr[0]=arr[i+1]
        arr[i + 1]=temp

print("mini=",arr[0])
