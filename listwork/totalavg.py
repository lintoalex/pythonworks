expenses=[12000,13000,11000,14000,15000,21000,22000,13000]

total_expenses=0

for i in range(0,len(expenses)):

    total_expenses=total_expenses+expenses[i]

    avg_expenses=total_expenses/len(expenses)

print(avg_expenses)


    