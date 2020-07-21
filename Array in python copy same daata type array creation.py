#import array as arr
# hm ye tb use krty han jb hm ny sirf same type ki array bnani ho
#otherwise hmy pta ha array python may different type ki b ho skti ha

#import array
from array import *  #array k sary functions import krnan chahty han


values=array('d',[1.2,1.3,1.5,12.3])  #is may first typecode(which type),osi type k elements
#f stand for float also i stands for int but there are differenr keywords for diff
#data type


#signed values:start from negTIVE TO POSITIVE(TYPECODE =i)
#UNSIGNED VALUES:ONLY POSITIVE  (TYPECODE=I)

for i in range(len(values)):  #if we don't know the size of array we can taek it by len(arrayname)

    print(values[i])  #printing values index by index

values.reverse();#reverse the array
print(values)

# how to copy one array into an other

newarray=array(values.typecode,(a for a in values))
#jb hm kis array ko copy krty han to pr wali line os ka syntex ha

print(newarray)

newarray=array(values.typecode,(a*a for a in values)) #sqaure of number
#jb hm kis array ko copy krty han to pr wali line os ka syntex ha

print(newarray)
j=newarray[0]

print(len(values))#array ka size



#sorting of array
# val = array('i',[4,2,8,1,7])
# val = array('i', sorted(val))

val = array('d', sorted(newarray))
for i in range(len(val)):
  print(val[i])




