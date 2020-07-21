#in array funtion we don't have concept of multiple dimens array so
#we use numpy for multiple array
#we can work with numpy for both single or multiple dimension the only differenecv here
#is you just need to change the syntax for single dimension array
#arr=array('i',[1,2,3],[2,1,4])->arr=array([1,2,3],[2,1,4])We dont need toi tell the
#data type of array
from numpy import *

arr=array([1,2,3,2,1,4],int)#array('i',[1,2,3,2,1,4]) in numpy this will be the error
print(arr)

# We have 6 ways to create arrays in numpy:
# array()
# linspace()
# logspace()
# arange()
# zeros()
# ones()




#1-array () method

arr=array([1,2,3,54,5])

print(arr)
print(arr.dtype)#type of values


#2-linspace () method

arr=linspace(0,15,16)#arguments=start,end,its optional:how many parts you want to divide the values

print(arr)
print(arr.dtype)#type of values


#3-arange () method

arr=arange(0,15,2)#arguments=start,end,how many values you want to skip

print(arr)
print(arr.dtype)#type of values


#4-logpsace () method

arr=logspace(1,40,5)#arguments=start 10^1,end 10^40,How many parts of the values

print(arr)
print('%.2f' %arr[0])   #two digit answer
print(arr.dtype)#type of values



#5-zeros () method

arr=zeros(5,int)#It will give you 5 number of zeros,by defualt the values are
#float if you mention int it will give you only integer values
print(arr)


#6-ones () method
arr=ones(5,int)#It will give you 5 number of zeros

print(arr)



