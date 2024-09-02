
from re import fullmatch

variable_name=input("enter name ")

pattern="[a-zA-Z][a-zA-Z0-9_]*"

match=fullmatch(pattern,variable_name)

print("invalid" if match==None else "valiad")