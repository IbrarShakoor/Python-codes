#Multip threading:We use dthis just to run two codes or two statements simultaneously
#check the below example

from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)#ye 1 second sleep krwaye ga execution ko

class Hi(Thread):#We need to add this keyword in both classes so they can run parallel
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)  # ye 1 second sleep krwaye ga execution ko


t1=Hello()
t2=Hi()

# t1.run()   in k function ko call krny k bajay t1.start() ko call krna ha is ka mtlb same ha t1.run
# t2.run()
t1.start() # It must be called at most once per thread object. It arranges for the
#       object's run() method to be invoked in a separate thread of control
sleep(.2)
t2.start()

t1.join()#  Wait until the thread terminates.
t2.join()

#ye join keyword boly ga main thread ko wait until the both threads terminates complately then
#you can run Bye statement
print("Bye")