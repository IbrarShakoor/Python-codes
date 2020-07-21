

def sort(list):

    n=len(list)
    for i in range (n):
        print("Values of i:",i)
        minpos=i
        for j in range(i,n):
            print("Values of j:", j)
            if(list[j]<list[minpos]):
                minpos=j

        t=list[i]
        list[i]=list[minpos]
        list[minpos]=t

        print(list)





list=[2,4,1,3,77,5]
sort(list)