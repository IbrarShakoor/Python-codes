#polymorphism means many ways of representing objects:
# In python there are 4 ways:
# 1-Duck Typing,Operator Overloading,function/Method overloading,Method overriding
# x=5
# x="Ibrar"
# print(x)
                            #Duck type

class pycharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
            def execute(self):
                print("Compiling")
                print("Running")
                print("Spell Checking")
                print("Memory checking")

class laptop():
    def code(self,ide):
        ide.execute()



# ide=pycharm()Hm ide ki type change b kr skty han jasy agly step may hm ny Myeditor ko call
#kiya to ide os ka execute fucntion exy=ecute function krwye ga
ide=MyEditor()
lap1=laptop()
lap1.code(ide)
