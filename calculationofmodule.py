def add(a,b):
    return a+b

def mul(a,b):
    return a*b

def div(a,b):
    if a<b:
        a,b=b,a
    return a/b

def sub(a,b):
    if a<b:
        a,b=b,a
    return a-b
