from numpy import *
arr1=array([
           [12,33,3,2],
           [2,3,5,32]
           ])  # Two dimensional array

print(arr1)
print(arr1.ndim)#for dimension
print(arr1.dtype)
print(arr1.shape)#it will tell you about row and column
print(arr1.size)#no of elements

#How can we create muti dimension array to single dimension array?

print()
arr2=arr1.flatten()#it will flat the whole array and make one dimension array
print(arr2)


#How to convert into required no of r,c
print("You can pass number of rows,colmun:")
print()
arr3=arr2.reshape(2,4)#it will flat the whole array and make one dimension array
print(arr3)


print()
#how to convert into matrix ?
m=asmatrix('1,2,2;4,5,6')
print("Matrix:",m)

m=asmatrix(arr1)   #Matrix form
print("Matrix:",m)


m=asmatrix('1,2;2,3;4,5;6,8')#; will break the rows and make a new row
print("Matrix:",m)


print()

#We can use the same function with matrix which we use with array
print(diagonal(m))#Only diagonal elements printing
print(m.min())
print(m.max())


print()
print("Matrix Operations:")
m1=asmatrix('1,2,3;2,3,4;1,4,4')
m2=asmatrix('1,7,7;1,2,3;2,3,4')

sum=m1+m2
print("Matrix sum=",sum)


mul=m1*m2
print("Matrix Multiplication=",mul)


print()




