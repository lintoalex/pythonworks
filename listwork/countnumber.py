
number=[22,99,77,22,44,55,22,77,55,44,55,99,22,44]

numbers_count={}

for t in number:

    if t in numbers_count:

      numbers_count[t]+=1

    else:

       numbers_count[t]=1

print(numbers_count)  


