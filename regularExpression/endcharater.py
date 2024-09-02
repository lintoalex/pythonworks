
from re import findall

text="the fat cat run very fast to catch rat"

pattern=".at"

match=findall(pattern,text)

print(match)