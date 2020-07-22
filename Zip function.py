names=("Ibrar","Raja","IBM")  #tuples
names1=("Hana","Raja","IBM")



zipped=list(zip(names,names1))#Join kr k list may bna diya ha
print(zipped)#hm use krty han ye zip fun combine krny k liye


zipped=set(zip(names,names1))#Join kr k list may bna diya ha
print(zipped)

zipped=dict(zip(names,names1))#Join kr k list may bna diya ha
print(zipped)


zipped=zip(names,names1)
for (a,b) in zipped:
    print(a,b)

