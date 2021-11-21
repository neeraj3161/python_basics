from random import choice


list_1 = [1,2,4,5,6,7,8,8,9,'A','C','D','E','X']
print("Lottery ticket which won is",end=" ")
for i in range(1,5):
    ticket=choice(list_1)
    print(f'{ticket}',end="")


print("\nYou won this ticket after performing "+str(i)+" loops")




