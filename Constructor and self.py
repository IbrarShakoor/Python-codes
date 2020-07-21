
class Computer:

    def __init__(self):#hm kisi b method ko object k sath call kre skrty han
      self.name="Ibrar"
      self.age=23
    def update(self):
        self.age=993
    def compare(self,c2):   #yahan pe jo self ha wo c1 a rha ha
        if self.age==c2.age:
            return True
        else:
            return False

c1=Computer()  #c1=object name have access fro any variables/function  ,Computer() is acting like a constructor
c2=Computer()
print(c1.name)
print(c2.name)

print()
c2.name="Raja"
c1.update()
print(c1.name)
print(c1.age)


print()
print(c2.name)
print(c2.age)

if  c1.compare(c2):
    print("They are same")
else:
    print("Not same")







