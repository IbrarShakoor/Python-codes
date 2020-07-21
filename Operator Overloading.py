#operator Overloading=new definition to give nay operator


class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self, other):

        m1=self.m1+other.m1
        m2 = self.m2 + other.m2
        s3=student(m1,m2)

        return s3
    def __gt__(self, other):#These keywords are predefine in python
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        if(m1>m2):
            return True
        else:
            return False

    def __str__(self):
        return  '{}   {}'.format (self.m1,self.m2)  #ye format is liye diya ha
        #k wo neechy values string may print ho jaien





s1=student(40,45)
s2=student(444,47)


s3=s1+s2#ye objects in k liye + ki definition hood sy define krni pry gi so lets do it


print("Sum is :")
print("M1=",s3.m1,"M2=",s3.m2)


print()
if(s1>s2):
   print("S1 wins")
else:
    print("S2 wins")


print()
a=100



print(a)#these are same =print(a.__str(self)#printing value

#print(s1.__str__())   #we define the function on the top for objects thats why its printin the values
#of object

print(s1.__str__())
print()

#in ko print krwany k lie opr format diya ha kyu k by default print() function
#prints only strings
print(s1)  #=print(s1.__str__())   same
print(s2)