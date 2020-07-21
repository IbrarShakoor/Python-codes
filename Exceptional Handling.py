#Compile tim error
#Logical Error
#Runtime Error


a=120
b=4

#Exception Handling
try:
    print("resource open")
    print(a/b)
    k=int(input("Enter the num:"))
    print(k)

except ValueError as e:  #hm koch be exception handling may set kr skty han
    print(e)
except ZeroDivisionError as e:
    print("Hey,you can't divid eby 0")
    print("Hey,you can't divid eby 0",e)#e will give you error name which is built in


except Exception as e:#ye Exception keyword sbi error check kry ga koch b error ho ga
    #wo return kr dy ga
    print(e)

finally:
    print("Jo b hi jay finally may likhi statement execute ho gi")
    print("resource closed")