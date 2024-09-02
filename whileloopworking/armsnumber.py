 
num=int(input("enter number"))
org=num

total=0

digit_count=len(str(num))

while(num !=0):

    digit=num%10

    exponent=digit**digit_count

    total=total+exponent

    num=num//10

print("is amstrong number" if org==total  else "is not amstrong number" )
