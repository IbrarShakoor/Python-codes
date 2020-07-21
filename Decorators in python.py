
def div(a,b):
    print(a/b)


def docr_fun(div):#yahn pe hm ny div pass kiya
    def inner(a,b):#ye wo fun ha jo div ki value ko change kry ga or is fun ko div fun ki access ha
        if a<b:
            a,b=b,a
        return div(a,b)#yahan hm ny dev return kiya inner ko

    return inner#innert return kia docr_fun ko

div1=docr_fun(div)

div1(2,4)

# f=div(4,6)
#
# print(f)
#

#what if we want to keep this condition like a>b if user put a<b we can execute
# in a a>b way

# For thsi purpose we can use if(a<b):a,b=b,a

#But we can also use new technique which is called decorator, these decorators can make new fun
# to give some more values/functionality to old function.  Ex below:


