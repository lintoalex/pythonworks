
from re import finditer

text="abc 7Klefg@#"

# pattern="\\D"

# matcher=finditer(pattern,text)

# for m in matcher:

    # print(m.start(),"==",m.group())


# pattern="\\w"

# matcher=finditer(pattern,text)

# for m in matcher:

#     print(m.start(),"==",m.group())

# pattern="\\W"

# matcher=finditer(pattern,text)

# for m in matcher:

#     print(m.start(),"==",m.group())

# pattern="\\S"

# matcher=finditer(pattern,text)

# for m in matcher:

#     print(m.start(),"==",m.group())

pattern="\\S"

matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"==",m.group())


# pattern="\\d""[a-zA-Z0-9]"
# pattern="\\d""[^0-9]"