
number=[12,3,2,5,7,11,10,4]

largest_num=number[0]

second_largest_num=0

for i in number:

    if i > second_largest_num and i > largest_num:

        second_largest_num = largest_num

        largest_num = i

    elif i> second_largest_num and i<largest_num:

        second_largest_num=i

print(f" second largest number {second_largest_num}")