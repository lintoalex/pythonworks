#claculate monthly emi

principal=80000

interest_rate=14

time=6 

monthly_rate=interest_rate/(12*100) 

months=time*12

emi=(principal*monthly_rate*(1+monthly_rate)**months/((1+monthly_rate)**months-1)) 
     
print("number of months",months)

print("emi per months",emi)

total_amount=emi*months

total_interest=total_amount-principal

print("total interest amount",total_interest)

print("total payable amount",total_amount)