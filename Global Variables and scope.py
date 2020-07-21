a=10  #Global var

def fun():
    a=17#Local Var
    print("In fun:",a)

fun()

print("Outside:",a)

print()
#how to change the global value by local fun?
def fun():
    global a   #hm ny compiler ko bola ha k ye global a ha is or hmy isy change krna ha
    a=17#Local Var
    print("In fun:",a)#is mehtod ka ye ha hm is k badd jb b a ki value change krerin gy
    #to global ki value change hoti jay gi

fun()

print("Outside:",a)

b=100
print()
#another way to use local and global value in the same local fun:

def fun():

    b=107#Local Var
    #x=globals()['b']  #ye global fun jitni b global values hon gi sb x ko assign kry ga
    #agr ap ny kisi specific var ki value assign krwani ho to sath may #
    #os ka name likh dein
    # print("In fun x:", x)
    # print("x ki id:",id(x))
    print("In fun b:", b)
    print("b ki id:", id(b))


    globals()['b']=1000  #yahan hm ny global var ki value change kr di

fun()


print("Outside:",b)