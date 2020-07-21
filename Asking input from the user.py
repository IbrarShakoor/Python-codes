a=int(input("Enter the 1st value:"))
b=int(input("Enter the 2nd value:"))


# In pyth0n when we want to take
# input from the user we use "input()" function but the condition is input
# function always take data and give data in string data type.

# So everytime whenever you wanna use input function and want to use data
# into another data type you have to convert the data type in to required data type.
#
# a=input("Enter the 1st number:") //be dehault data type here is string
# x=int(a)        //converting from str ti int
# b=input("Enter the 2nd number:")
# x=int(b)
z=a+b
print("Integer sum=",z)

# how to ask character becaus ethere is no char data type in pythin but we cam make it

#ch=input("Enter the char:")[0]#but ye hmy str dy ga hmy ak char print krwana ha
#or user ko bound b rakhna ha to is k bht sy tareeky han

ch=input("Enter the char:")[0]#ye sirf pehla char he ch may store kry ga or
#osy print kr dy ga
print("Char is :",ch)
print("\nChar is :",ch[0])#ak or method ha
