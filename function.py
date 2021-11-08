def fucn1():
    print("I am a function")

fucn1()
print(fucn1())
print(fucn1)

def func2(arg1,arg2):
    print(arg1," ",arg2)

#     none printed because there is no return value

def cube(x):
    return x*x*x

# print(func2(10,20))
# print(cube(3))

def power(num,x=1):
    result =1
    for i in range(2):
        result = result*num
    return result

print(power(2))
print(power(20,1))


for j in range(2):
    print(j)

def multi_add(*args):
    result=0
    for x in args:
        result = result+x
        return result

print(multi_add(23+23+23+23+23))
