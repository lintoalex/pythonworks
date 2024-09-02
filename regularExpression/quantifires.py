
from re import finditer

text="ab12xyz678#$pqr123"

pattern="[0-9]{3}"

matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"==",m.group())

    
text="ab12xyz678#$pqr123"

pattern="([a-z]|[0-9])"

matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"==",m.group())