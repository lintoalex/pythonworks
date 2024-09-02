
year=int(input("enter year"))

print("is yaer leap" if year%100==0 and year%400==0 or year%100 !=0 and year%4==0 else "not leap year")
