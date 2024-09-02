
from json import load

f=open("C:\\Users\\linto\\OneDrive\\Desktop\\PythonJuneWorks\\jsonWorks\\filims.json")

product=load(f)

for i in product:

 print(i.get("title"))