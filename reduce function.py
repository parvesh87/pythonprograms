import functools
x=[10,15,20,25,28+2]

def add(a,b):
    return a+b
g=functools.reduce(add,x)
print(g)
