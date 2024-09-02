
from re import fullmatch

text=input("enter pancard no")

pattern="[A-Z]{3}[PACAFHT][A-Z][0-9]{4}[A-Z]"

matcher=fullmatch(pattern,text)

print("invalid" if matcher == None else "valid")