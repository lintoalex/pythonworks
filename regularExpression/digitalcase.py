
from re import finditer

text="abc123 @K7LMdef"

pattern="[0-9]"

matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"==",m.group())


pattern="[a-z,A-Z,0-9]"

matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"==",m.group())