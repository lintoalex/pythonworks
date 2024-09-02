
f=open("C:\\Users\\linto\\OneDrive\\Desktop\\PythonJuneWorks\\FileWork\\students.txt","r")

students=[]

for stu in f:

    students.append(stu.rstrip("\n"))

print(students)