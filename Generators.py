#Generators same hoty han iterators ki trah mgr ye ak ak value return krty han mtlb pehly 1st
#phr next then next


def topten():
    n=1
    while(n<=10):
        s=n*n
        yield s
        n+=1


values=topten()
for i in values:
    print(i)