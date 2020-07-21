#Methods ki 3 types han
#1-instance,class,static

class Student:
    Schoolname="BME"  #class var
    def __init__(self,m1,m2,m3):#instance var
        self.m1=m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def show(self):
        print("m1=",self.m1)
        print("m2=", self.m2)
        print("m3=",self.m3)

    #ye class method ha jb b hm nu class var ko access krna ho function k through to
    #class var k liye class function hota ha
    #synytax
    # @classmethod
    #def funname(cls):

    #nichy call krny ka treeka  classname.functionname

    @classmethod
    def getschool(cls):
        return cls.Schoolname



    #ye static method ha isy tb use krty han jb koe irrelevant operation/fun krwana
    #ho class may
    #sysntx:
    # @staticmethod
    # def funname(nothing):

    # nichy call krny ka treeka  classname.functionname
    @staticmethod
    def fact(n):
        f=1
        for i in range(1,n+1):
          f=f*i

        return f

c1=Student(22,34,55)
c1.show()
print()

r=c1.avg()
print("Avg",r)
print()


print("Factorial")
r1=Student.fact(4) #nichy call krny ka treeka  classname.functionname
print("Fact=",r1)


print()
print(Student.getschool())#nichy call krny ka treeka  classname.functionname
