#anonymous function =without name
#We can create the function without nam ein python

#These funtions are anonymous they dont have any name and they use in python
#we can pass these fun to other functions;


#Syntax is:           anyname=  lambda arguments :operation
#This lamda is a keyword also functions are objects in python so we can return value in
#var which is anything
#Example is below:
#
r= lambda  a,b: a*b #here r is kind of nam eof unction but originally function is anonymous



a=int(input("Enter the values of a:"))
b=int(input("Enter the values of b:"))
f=r(a,b)


print("R=",f)


#We can use anonymous fun with others built in funcs:
# filter()
# map()
# reduce()


# Example:


nums=[1,2,4,65,7,7,44,66,22]

evens=list(filter(lambda a:a%2==0,nums))

print(evens)


#If i want to make it double,which I got


n=list(map(lambda a:a*2 ,evens ))

print("Doubles:",n)

from functools import reduce
#if we want to reduced the data

sum=reduce(lambda a,b:a+b,n)  #We use this function to reduced the value

print("Sum=",sum)
