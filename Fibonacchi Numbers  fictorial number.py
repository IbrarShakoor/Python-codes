import sys  # just to check the limit of recursion function



def fib(n):
    a = 0
    b = 1
    j=0
    list=[]
    if(n<0):
        print("Invalid Entry")
    elif(n==1):
        print(a, end=" ")
    elif(n==2):
        print(a, end=" ")
        print(b, end=" ")
    else:
     print(a,end=" ")
     print(b,end=" ")
     for i in range(2,n):#2 sy start ho ga or n-1 tk jay ga
        lt = []
        c=a+b
        a=b
        b=c
        print(c,end=" ")



x=int(input("Enter the num :"))

fib(x)



#Fact by for loop
def fact(n):
    f=1
    for i in range(1,n+1):
      f=f*i

    return f


print()
n=int(input("Enter the num :"))
result=fact(n)

print(result)

print("By default value:",sys.getrecursionlimit())#is sy hmy ye pta chly ga k recusrion ki be default kitni limit ha



#Fact by for recursion
def f(n1):
    if n1==0:
        return 1
    else:
       return n1 * f(n1-1)


print()
n1=int(input("Enter the num :"))
result1=f(n1)

print("Result by Recusrion:",result1)





# #we can chnage the limit by using this statement
# sys.setrecursionlimit(2000)# we are passing the numnber till which we want to increase the limit
