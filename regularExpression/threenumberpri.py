
from re import finditer

text="ab12xyz678#$pqr123"

pattern="([a-z]{3}|[0-9]{3})"

matcher=finditer(pattern,text)

for m in matcher:

   print(m.start(),"==",m.group())