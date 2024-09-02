 
# number=[1,3,2,5,7,9,10,4]

# smallest_num=number[0]

# for i in number:

#     if i < smallest_num:

#         smallest_num=i

# print(f" smallest number {smallest_num}")
 
number=[3,5,7,1,9,2,10,4]

smallest_num=number[-1]

secon_smallest=number[0 ]

for i in number:

    if i < secon_smallest and i < smallest_num:

        secon_smallest=smallest_num

        smallest_num=i

    elif i < secon_smallest and i > smallest_num:

        secon_smallest=i

print(secon_smallest)