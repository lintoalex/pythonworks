
# wap to find sum of odd number in the list

number=[1,2,3,4,5,6,7,8,22,20,33,31,21,23,45]

odd_number=[]

odd_sum=0

for i in number:

    if i%2 !=0:

        odd_number.append(i)

        odd_sum+=i

print(odd_number,"is odd number",odd_sum)