
from re import finditer

text="abc123 @K7LMdef*&^%"

pattern="[^A-Za-z0-9\\s]"

match=finditer(pattern,text)

for m in match:

    print(m.start(),"==",m.group())