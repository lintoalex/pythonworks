
from re import fullmatch

text="31"

pattern="([0?[1-9]|1[0-9]|2[0-9]|3[0-1])"

matcher=fullmatch(pattern,text)

print("invalid" if matcher == None else "valid")