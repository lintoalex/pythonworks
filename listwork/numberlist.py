
number=[10,11,12,34,43,54,19,78,42]

# print(len(number))

# for i in range(0,len(number)):

#     if number[i]%2==0:

#        print(number[i])

# total=0

# for i in range(0,len(number)):
           
#     total+=number[i]

# print(total)


odd_total=0

for i in range(0,len(number)):

    if number[i]%2 !=0:

        odd_total+=number[i]

print(odd_total)

