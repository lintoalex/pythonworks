number=int(input("enter number"))

fact=1

for i in range(1,number+1):

    fact=fact*i

print(f"{number}!={fact}")