
from re import fullmatch

f=open("C:\\Users\\linto\\OneDrive\\Desktop\\PythonJuneWorks\\regularExpression\\domain.txt","r")

pattern="[\\w\\W]+\\.com"

for line in f:

    domain=line.rstrip("\n")

    matcher=fullmatch(pattern,domain)

    if matcher !=None:

        print(domain)