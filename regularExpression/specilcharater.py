

from re import finditer

text="abc123 @K7LMdef"

pattern="[^A-Za-z]"

matcher=finditer(pattern,text)

for m  in matcher:

    print(m.start(),"==",m.group())