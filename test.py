import random
L = []
for i in range(0,8):
    var = input("please enter a name :")
    L.append(var)

index = random.randint(0,7)
randomperson = L[index]
print("the choosen name is" , randomperson)
