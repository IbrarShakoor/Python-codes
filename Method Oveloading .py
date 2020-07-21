#Method Overloading:There is no method overloading in python we just use some tricks
#and make fullfillments of method overloading :We can use if,else,also b* which can takes
#so much arguments that's it


class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

        #technique of method overloading
    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s



s1=student(40,45)
s2=student(444,47)

print(s1.sum(22,33))
print(s1.sum(22,33,77))
print(s1.sum(22))
