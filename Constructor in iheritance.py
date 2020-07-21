class A:#parent class
    def __init__(self):
        print("Contructor of A")
    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
            print("Feature 2 is working")

# class B(A):#child class  means after writing Ain brackets we can say B ki access ha A k abi attributes/fun per
#             def __init__(self):
#                 super().__init__()
#                 print("Contructor of B")
#
#                 def feature3(self):
#                     print("Feature 3 is working")
#
#                 def feature4(self):
#                     print("Feature 4 is working")

class B():  # child class  means after writing Ain brackets we can say B ki access ha A k abi attributes/fun per
        def __init__(self):

            print("Contructor of B")

            def feature3(self):
                print("Feature 3 is working")

            def feature4(self):
                print("Feature 4 is working")


class C(A,B):

    def __init__(self):
        super().__init__()#it will always call from left to right ,so it will call constuctor of A
        print("Constuctor in C")
    # child class  meand after writing Ain brackets we can say B ki access ha A k abi attributes/fun per
    def feature5(self):
        print("Feature 5 is working")

    def feature6(self):
        print("Feature 6 is working")

    def feat(self):
        super().feature1()


a1=A()#it will call the contsructor of A

print()
a1=B()#it will call the contsructor of B, agr b may constructor ni ha __init(self)
#to ye phr A ka constructor inherit kry ga ,jb b hm B ka object bantay han to ye sb sy pehlky
#B may constructor dakhta ha agr ha to exxxute kr diya agr ni to A sy ly kr execute kr diya
#Agr hm ny both constructgor ko access krna ha to hmy keyword used krna pry ga
#child class B may which "super().__init()"  In this way you can call boith constructor

print()
a1=C()#Wehen we  use super().__init__()in C construtor it will always call A's
#constructor because there is one technique  Method Resolution Order (MRO).It's saying that
# during inherritance the child class will always take features from left to right


print()
a1.feat()
#with the help of super().__init__()print we can all both constructor and also methods of
#parent class