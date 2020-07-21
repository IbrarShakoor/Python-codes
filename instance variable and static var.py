
#asy var jo class may define kiye jain mgr __init sy outside ony static/class var kehty han
class car:
    wheels=5#ye class/Static variable ha os isy sgr hm ny change krna ho to classname.varname
    def __init__(self):#These var are instanec/Object variables
     self.com="BMW"
     self.Model=2019
     self.color="Black"



c1=car()


print(c1.Model)
print(c1.color)
print(c1.com)
print(c1.wheels)

car.wheels=100
print(c1.Model)
print(c1.color)
print(c1.com)
print(c1.wheels)


