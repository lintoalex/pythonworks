
f_read=open("C:\\Users\\linto\\OneDrive\\Desktop\\PythonJuneWorks\\FileWork\\years.txt","r")

f_century=open("C:\\Users\\linto\\OneDrive\\Desktop\\PythonJuneWorks\\Fileoperations\\century_year.txt","w")

f_non_century=open("C:\\Users\\linto\\OneDrive\\Desktop\\PythonJuneWorks\\Fileoperations\\non_century_year.txt","w")

for year in f_read:

    y=int(year.rstrip("\n"))

    if y%100==0:

     f_century.write(str(y)+"\n")

    else:
   
     f_non_century.write(str(y)+"\n")