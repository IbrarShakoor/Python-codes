
class Student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()#yahan hm ny inner class kaobject bnaya ha outer class k andder
        #hm bahir b bna skty han os k liey nichy dekho

    def show(self):
        print(self.name , self.rollno)
        self.lap.show()#calling inner class function

    class Laptop:#inner class

        def __init__(self):
            self.brand = "Hp"
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand,self.cpu,self.ram)


s1 = Student('Navin',2)
s2 = Student('Jenny',3)

s1.show()

#inner class ka object outside the main class bnaya
lap1 = Student.Laptop()
print()
print(s1.lap.ram)
print(s1.lap.brand)
# lap1 = s1.lap
# lap2 = s2.lap
#
# print(id(lap1))
# print(id(lap2))


#inner class k var access
