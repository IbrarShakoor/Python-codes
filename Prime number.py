x=int(input("Enter the number:"))
i=1
count=0
print(x)
for i in range(2,x+1):
    if(x%i==0):
        count=count+1
        print("i=",i)
if(count==1):
    print("Numbers are prime")
else:
    print("No prime")