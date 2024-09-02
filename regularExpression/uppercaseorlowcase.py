
from re import finditer

text="abc123 @K7LMdef"

pattern="[A-Za-z]"

matche=finditer(pattern,text)

for m in matche:

    print(m.start(),"==",m.group())

    pattern="[^a-bA-Z]"

    matcher=finditer(pattern,text)

for m  in matcher:

    print(m.start(),"==",m.group())