#By default python doesn't have abstrct class system but we can create it with the help of ABC()
# class which is Abstract class.Also We cant create the object of abstract class
# .If we inherit another class from abstrct class still we can't create its objects only


from abc import ABC,abstractmethod

class computer(ABC):#passing ABC this class became abstract also inorder to make abstrct function
    #we need to define decorator @abstractmethod above the function
    @abstractmethod
    def process(self):
        pass
        
        
class laptop(computer):#this class is inheriting abstract class we need to give the
    #definition of abstract funtion here otherwise it won't work
    def process(self):
        print("Running")


class whiteboard():
    def write(self):
        print("it's writing")




class programmer:
    def work(self,com):
        print("Solving Prob")
        com.process()

# com=computer()#As the class isabstrct so we can't create it's object
com1=laptop()#We can only create the object of that class which is iherited by abstrsct class
#if we are giving the body of abstrct fun in the other class liuke in laptop class
com2=whiteboard()

com1.process()


prob1=programmer()
prob1.work(com1)







