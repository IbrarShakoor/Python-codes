av=20
i=1
x=int(input("How many candies you want:"))
                     #break example
while(i<av):
    if(x<=av and i<=x):
     print("Candies")
     i+=1
    elif(x>av):
     print("out of stock")
     break  #it will jump out of the loop

               #contniue example

print("\n\n")
for i in range(100):
      if(i%3==0):
        continue    #it will skip the loop and will go back to the start of teh loop
      print(i, end=" ")

                 #pass example


for i in range(101):
      if(i%2!=0):
          pass  #pass is just to say to the programme I haev nothing to write
                #just to say skip it dont do anything
      else:
         print(i)
