
from re import fullmatch

variable=input("enter name")

pattern="[k-m][369][a-zA-Z0-9@]*"

matche=fullmatch(pattern,variable)

print("invalid" if matche == None else "valid")