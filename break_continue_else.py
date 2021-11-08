# for n in range(2,10):
#     # print(n)
#     for x in range(2,n):
#         # print(x)
#     #     if n%x==0:
#     #         print(n,'equals',x,"*",n//x)
#     #         break
#     # else:
#     #     print(n, ' is a prime number')

# prime number are only divisible by itself and 1
for n in range(1,1000):
    # print(n)
    for x in range(2,n):   #here the range for n will be 9 means 2 till 8 it will check all the numbers
        if n%x==0:
            print(n, 'equals', x, '*' , n//x)#// is floor division it rounds up the fraction
            break
    else:
        print(n,end=" ")




# a simple example
# for x in range(2,10):
#     if x==4:
#         print(x)
#         break
#
#     else:
#         print('x is not 4')


for num in range (2,10):
    if num %2==0:
        print("found a even number", num)
        continue
    print("Found a odd number", num)