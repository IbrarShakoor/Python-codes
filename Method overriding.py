class A:
    def show(self):
        print("I am in A")


class B:
    def show(self):
        print("I am in B")

a1=A()
a1.show()  #yahan pe wo A k show k sath attch ha

a1=B()#yahn pe hm ny osy override kr diya same function k name sy
a1.show()#yahan wo B ka show kry ga