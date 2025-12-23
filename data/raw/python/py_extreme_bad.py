# TERRIBLE PYTHON CODE - Anti-patterns everywhere

import os, sys, time
x=[]
y=[]
z=[]

def a(p):
    if p>0:
        if p>1:
            if p>2:
                if p>3:
                    if p>4:
                        if p>5:
                            print("bad")

def b(s):
    # TODO fix
    # FIXME broken
    # TODO dangerous
    # FIXME needs work
    eval(s)

def c():
    try:
        x = [1,2,3]
        return x[100]
    except:
        pass

def d():
    global x,y,z
    x = 1

def e(a, b, c, d, e, f, g):
    if a:
        if b:
            if c:
                if d:
                    if e:
                        if f:
                            if g:
                                return a+b+c+d+e+f+g

def main():
    a(10)
    b("test")
    c()
    d()
    e(1,2,3,4,5,6,7)

if __name__=="__main__":
    main()
