class A:#parent class
    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
            print("Feature 2 is working")

class B:#child class  meand after writing Ain brackets we can say B ki access ha A k abi attributes/fun per
                def feature3(self):
                    print("Feature 3 is working")

                def feature4(self):
                    print("Feature 4 is working")

class C(A,B):
                         # child class  meand after writing Ain brackets we can say B ki access ha A k abi attributes/fun per
                        def feature5(self):
                            print("Feature 5 is working")

                        def feature6(self):
                            print("Feature 6 is working")


a1=A()
a1.feature1()
a1.feature2()

#Single Level:A->B
print()
b1=B()  #child class

b1.feature3()
b1.feature4()

#Multiple Level:A,B->C
print()
c1=C()  #child class from B
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
c1.feature6()