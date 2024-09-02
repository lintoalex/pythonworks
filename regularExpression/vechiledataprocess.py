
from re import fullmatch

f_read=open("C:\\Users\\linto\\OneDrive\\Desktop\\PythonJuneWorks\\regularExpression\\vechiledata.txt","r")

f_valid=open("C:\\Users\\linto\\OneDrive\\Desktop\\PythonJuneWorks\\regularExpression\\vechilenovalid.txt","w")

f_invalid=open("C:\\Users\\linto\\OneDrive\\Desktop\\PythonJuneWorks\\regularExpression\\vechilenoinvalid.txt","w")

pattern="(KL)(\\s)?[0-9]{2}(\\s)?[A-Z]{1,2}(\\s)?[0-9]{4}"

for line in f_read:

    vechile=line.rstrip("\n")

    matcher=fullmatch(pattern,vechile) 

    if matcher == None:

        f_valid.write(str(vechile)+"\n")

    else:

        f_invalid.write(str(vechile)+"\n")
    

