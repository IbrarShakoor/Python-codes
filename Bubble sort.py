
def sort(list):
      n=len(list)
      print("Length =",n)

      for i in range(n):#this loop is only for iterartion
          print("This is value of i", i)

          for j in range(0, n - i - 1):#this loop is for swapping
              print("This is value for j ", j)

              if list[j] >= list[j + 1]:
                  list[j], list[j + 1] = list[j + 1], list[j]
      return list



list=[2,4,1,5,62,2,1]

l=sort(list)
print(l)

