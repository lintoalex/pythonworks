
num=int(input("enter number"))

total=0

while(num !=0):

    digit=num%10

    num=num//10

    total=total+digit

print(total)    

