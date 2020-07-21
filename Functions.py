#functions

def greet():#definition of function
    print("Hello Bro")
    print("One line function")


greet()#Calling the function


print()
#How to sum by function
def sum(x, y):
    r=x+y
    sub=x-y
    #print(r)
    return r,sub   #in python we can retrun multiple values at a time from single function

result1,result2=sum(2,34)
result=sum(2,34)
print(result)

#both ways are correct,if you want to print value separate or together you can
#do both
print(result1)
print(result2)


#we don't use pass by value and pass by reference in python
def update(x):
    print("x id=",id(x))
    x=9
    print("x=",x)


update(7)
a=10
print("a id =",id(a))
update(a)
print("a=",a)
print("a id=",id(a))



def update1(list):
    print("list id=",id(list))
    list[0]=900
    print("In the function=",list)





list=[1,2,43,5]
print("list id=",id(list))
update1(list)

print("Outside the fun:",list)


print()
print("Typesof arguments")
print("1->Formal Arg    2->Actual Arg")

#passing value are called ->formal
#receiving values in the function are->Actual
#Actual arg has 4 more types:1-Position
# 2-Keword
# 3-Default
# 4-Variable length


def person(name,age=18):
    print(name)
    print(age)


person('Ibrar',23)#Correct position


#but what if we dont knwo the variabel position then we can use keyword
person(age=23,name='Ibrar')


#default arg:

person(name='Ibrar')#as we are not giving 2nd arg so it will take by default
#from the top which we described in the funtion

#variable length:

#hm ye concept tb uys krty han jb hm ny ak sy ziada values ko solve krny ho
#ya phr ak sy ziada values ak hi variables ko assign krni hom


def sum2(x,*y):#a has only fisrt value *y means all of the values are in y

    print("x=",x)
    print("y=",y)
    c=0
    #c=x+y  #hm ak value ko b ki 4 valuesmay add ni kr skty so ye arror ha
    for i in y:
        c=c+i

    print("sum=",c+a)

print()
sum2(22,223,4,5,7,22)#Yahan pe values bht ziada han to hm python k extra features ko us ekrein gy





print()
def person1(name,**data):
    print("Name",name)
    print("Data",data)
    print()

  #separate printing of data
    for i,j in data.items():
     print("Data", i,j)
person1("Ibrar",lastname="Shakoor",age=23,year=2020,work='Learning python')

#age hm dosry variabel jis may ak sy ziada value han os k liye keyword
#b bejna chahty han to ** use krein gy