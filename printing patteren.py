i,j=1,1
for i in range(4):
  for j in range(4):
    print("#",end="")
  print()


print("\n")
i, j = 1, 1
for i in range(5):
      for j in range(i):
          print("#", end="")
      print()


print("\n")
i, j = 1, 1
for i in range(4):
      for j in range(4-i):
          print("#", end="")
      print()

print("\n")
for i in range(4):

    for j in range(4-i):
        print(i+j+1, end="")
    print()

    print("\n")


l = ['A','B','C','D','P','Q','R']

for i in range(4):
    for j in range(4):
        if j<=i:
            print(l[j],end="")
        else:
            print(l[j+3],end="")
    print()

