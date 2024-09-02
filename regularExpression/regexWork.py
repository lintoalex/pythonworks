
from re import finditer

text="hellopythonhellopythonhellopython"

match=finditer("python",text)# return object (start,group)

count=0

for m in match:

    print(m.start(),"===",m.group())

    count+=1

print(count)

