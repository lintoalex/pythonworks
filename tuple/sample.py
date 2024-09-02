 
number=[1,2,[3,(100,200,300),4],5,6,]

# num=number[2][1]

# new_num=list(num)

# new_num.append(500)

# print(tuple(new_num))

# number[2][1]=tuple(new_num)

# print(number)

new=number[2]

else_four=new.pop()

new.insert(1,else_four)
print(new)

number[2]=new
print(number)

new1=number[2][2]
l=list(new1)
l.insert(1,150)
l1=tuple(l)
number[2][1]=l1
print(number)