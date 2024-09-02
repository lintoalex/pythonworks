num=int(input("enter number"))

previous=0

current=1

is_Fibo=False
next=previous+current

while(next<=num):
    next=previous+current

    previous=current

    current=next

    if num==next:
        is_Fibo=True
        break

print(is_Fibo)



