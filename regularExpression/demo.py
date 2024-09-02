

from re import finditer

text="ab12xyz678#$pqr123cdef"

pattern="([c-h]|[t-z])"

matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"==",m.group())