
# def nth_digit_max(num1,num2):

#    return num1 if num1%10 > num2%10 else num2

# print(nth_digit_max(127,450))


def nth_digit_max(num1,num2):
   
   digit=num1%10

   digit=num2%10

   if num1%10 > num2%10:
      
      return num1
   
   else:
      
      return num2
      
    

print(nth_digit_max(127,450))