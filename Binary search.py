
def sort(list):
    n=len(list)
    print(n)
    for i in range(len(list)):
          for j in range(0,len(list)):

            if(list[i]<list[j]):
                temp=list[i]
                list[i]=list[j]
                list[j]=temp
            else:
                pass

    return list

pos=-1
def binary_search(n,list):
    l=0
    u=len(list)-1
    while(l<=u):
        mid=(l+u)//2  #double slash just to get integer
        if(list[mid]==n):
            globals()['pos']=mid    #making mid var as global otherwise we can't access in bottom
            return True;
        else:
            if(list[mid]<n):#agr n bri ha mid sy to mid ko lower ko berha do
                l=mid+1
            else:
                u=mid+1
    return False

list=[2,43,6,2,66,6]


#shortcut way to sort your values
# list.sort()
# print(list)
l=sort(list)
print(l)

print()

n=int(input("Enter the number for search:"))

if binary_search(n,list):
    print("Found=",pos+1)
else:
    print("Not found")