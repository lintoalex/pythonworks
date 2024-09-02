
# wap to find the largest number 

number=[1,3,2,5,7,9,10,4]

largest_num=number[0]

for i in  number:

    if i > largest_num:

        largest_num=i

print(f"largest number print {largest_num}")