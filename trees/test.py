
#local variable 'a' referenced before assignment
# a= 1

# def hi():
#     a+=2
#     print(a)

# print(hi())

a= 1
print(id(a))

def hi():
    print(id(a)) #same id
    print(a) #1

print(hi())


a= 1
print(id(a)) #1818775650544
def hi():
    a=2
    print(id(a)) #1818775650576
    print(a) #2
    return a 

print(hi())
print(id(a)) #1818775650544


a= 1
print(id(a)) #1818775650544
def hi():
    a=2
    print(id(a)) #1818775650576
    return a 
a= hi()
print(id(a)) #1818775650576



a= [1]
print(id(a)) #1818778365184
def hi():
    a[0]+=2
    print(a) #[3]
    print(id(a)) #1818778365184

hi()
print(id(a)) #1818778365184


def outer():
    x = "local"

    def inner():

        
        print("inner:", x) #"local"

    inner()
    print("outer:", x) #"local"


outer()





#local variable 'x' referenced before assignment
def outer():
    x = "local"

    def inner():
        # nonlocal x
        
        print("inner:", x)
        x = "nonlocal"
    inner()
    print("outer:", x)


outer()



def outer():
    x = "local"

    def inner():
        nonlocal x
        
        print("inner:", x) #local
        x = "nonlocal"
    inner()
    print("outer:", x) #nonlocal


outer()


def outer():
    x = "local"

    def inner():
        # nonlocal x
        x = "nonlocal"
        print("inner:", x) #nonlocal

    inner()
    print("outer:", x) #local


outer()



def outer():
    global x
    x = "local"

    def inner():
        # nonlocal x
        x = "nonlocal"
        print("inner:", x) #nonlocal

    inner()
    print("outer:", x) #local


outer()
print(x)


x= "global"
def outer():
    global x
    x = "local"

    def inner():
        # nonlocal x
        x = "nonlocal"
        print("inner:", x) #nonlocal

    inner()
    print("outer:", x) #local


outer()
print(x) #local


x= "global"
def outer():
    # global x
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x) #"nonlocal"

    inner()
    print("outer:", x) #"nonlocal"


outer()
print(x) #"global"



class Solution:
    def __init__(self):
        self.res =1

    def test(self):

        self.res+=1
        return self.res

s=Solution()

print(s.res)
a=s.test()
print(a)
print(s.res)



print(None<4)
a=[1,2]
print(a[:0])