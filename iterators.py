num =[1,32,42]

for i in num:
    print(i)



print("\t\tBy iterator built in function:")
it=iter(num)#ye ak built in fun ha jo values ko iterate krta ha
print(it.__next__())#next valu k liye
print(it.__next__())
print(next(it))#ye dono same han =print(it.__next__())


print()


class topten:
    def __init__(self):
        self.count=1

    def __next__(self):
        if(self.count<=10):
         val=self.count
         self.count+=1
         return val
        else:
            raise StopIteration#itr will stop the iteration

    def __iter__(self):
        return self

print("\t\tBy making iteration class and acces the values:")
values=topten()
for i in values:
    print(i)



