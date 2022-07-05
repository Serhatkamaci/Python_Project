x=int(input("Bir boyut degeri giriniz : "))
d=""
for i in range(x):
    for j in range(x):
        if((i==0) or (i==(x//2)) or (i==x-1) or ((i>0 and i<(x//2)) and j==0) or ((i>(x//2) and i<(x-1)) and j==x-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("\n\n")
for i in range(x):
    for j in range(x):
        if(i==0 or i==x-1 or i==x//2):
            print("*",end=" ")
        else:
            print("*",end=" ")
            break
    print()
print("\n\n")
for i in range(x):
    for j in range(x):
        if((i<x and j==0 and i!=0) or (i==0 and j!=0 and j!=x-1) or (i>0 and  i<(x//2) and j==x-1) or (i==(x//2) and j>0 and j!=x-1)  or (i>(x//2) and j>(x//2))and i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("\n\n")
for i in range(x):
    for j in range(x):
        if ((j == 0 and i < x) or (j == x - 1 and i < x) or (i == (x // 2) and j > 0 and j < x - 1)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("\n\n")
for i in range(x):
    for j in range(x):
        if((i<x and (j==0 or j==x-1)) or (i==0 and j>0 and j<(x-1)) or (i==(x//2) and j>0 and j<(x-1))):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("\n\n")
for i in range(x):
    for j in range(x):
        if((i==0 and j<x) or (i>0 and i<x and j==x//2) ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()












