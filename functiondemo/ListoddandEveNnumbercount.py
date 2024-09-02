
# wap to find the count of even and odd number in list

number=[1,2,3,4,5,6,7,8,22,20,33,31,21,23,45]

odd_count=0

odd_number=[]

even_number=[]

even_count=0

for i in number:

    if i%2 == 0:

        even_number.append(i)
        even_count+=1
print(even_number,"even number count",even_count)


for i in number:

    if i%2 !=0:

        odd_number.append(i)
        odd_count+=1

print(odd_number,"odd number count",odd_count)

        
