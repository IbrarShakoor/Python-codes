x=19
y=26
print("x=",x ,  "y=",y)

z=x+y
print("z=",z)

print("Swap using third variable\n")
print("Number swapped:")
z=x
x=y
y=z
print("x=",x ,  "y=",y)

z=x+y
print("z=",z)
#akser ye question pochty han k swap kr k dikhao without 3rd variables
# so hm ye technique use kr skty han
x=x+y  #45
y=x-y  #26
x=x-y   #19


print("Swapped values with formula(without 3rd variable:")
print("x=",x ,"y=",y)


#akser ye question pochty han k swap kr k dikhao without 3rd variables
# also without using two lines so hm ye technique use kr skty han
print("Swapp using one line")

x,y=y,x
 #  x,y = y,x
#programme hemesha right side sy execuet hota ha so jb hm ny
 # dakha k stack may pehly x phr y ja rha ha mgr assigbement may jb stack
 #sy values nikalty han to top value x ko milay gi or bottom value Y ko
print("Swapped values with one line:")
print("x=",x ,"y=",y)