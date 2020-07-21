
def search(x,list):

    for i in list:
        if (list[i]== x):
            print("Element exist which is=", list[i])
            break
        else:
            print("Element don't exist ")
            break


list=[1,23,4,6,88,4]
x=int(input("Enter the number you want to search:"))


search(x,list)


