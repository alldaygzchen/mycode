# test 1 
a = []

def test():
    a.append(1)

test()
print(a) #[1]

# test 2 
a = []
def test(b):
    b.append(1)

test(a)
print(a) #[1]

# test 3
a = []
test(a)
test(a)
test(a)
test(a)
print(a) #[1, 1, 1, 1]

# test4
test ='abc'
print(test[:0])
set('abc')
set(['abc'])
set(['a','b','c'])
[1,2,3][:]