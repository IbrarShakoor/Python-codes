# for loop work with sequence

x=["Ibrar","a",1,7.0] #i jo ha wo shoro may hood hi first value ko k index pe ha
#jb hm kahin gy i in x it means for loop hood hi increase or decrease kry ga
for i in x:
    print("values:",i)

print("\n\n")
a="Ibrar Shakoor"
for i in a:   # we can also say that for i in "Ibrar Shakoor"
    print("Letter:",i)

print("\n\n")
for i in range(10):
        print(i,end="")

print("\n\n")
for i in range(11,22,3):
    if(i%5!=0):
     print(i, end="")


print("\n\n")
for i in range(100):
    if(i%5!=0 and i%3!=0):
     print(i, end=" ")