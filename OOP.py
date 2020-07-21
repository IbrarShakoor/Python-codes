class Computer:
   #How to decsribe variables/Attributes:We always need to define our var by __init__(self)

   #jb b hm ny python may koe var definer krna ho class k andr hmy hamseha is fun
   #k ander krna ha also function hamesha self argu leta ha,also jo self ha wo object
   #hota ha is case may com,com1

   def __init__(self,cpu,ram):#It will call automatically
       self.cpu=cpu
       self.ram=ram



   def config(self):
       #print("i3,16gb,1TB")
       print("CPU", self.cpu)
       print("Ram", self.ram)


cmp=Computer("i5","8gb")#Object Creation
cmp2=Computer("Razen 3",'4')#Object Creation

# Computer.config(cmp)  #Using the class name.fun
# Computer.config(cmp2)


cmp.config()   #using the object name.fun
cmp2.config()



