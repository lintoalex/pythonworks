
from re import finditer

text="abc123 @K7LMdef"

pattern="[abd]"

matcher=finditer(pattern,text)

count=0

for m in matcher:

    # print(m.start(),"===",m.group())

    count+=1

# print(count)

#------------------------------------------------------------------------------------------------------

pattern="[abd]"


matcher=finditer(pattern,text)

for m in matcher:

    # print(m.start(),"==",m.group())
#--------------------------------------------------------------------------------------------------------------
   
    pattern="[a-k]"

    matcher=finditer(pattern,text)

    for m in matcher:

        print(m.start(),"==",m.group())


