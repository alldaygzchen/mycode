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