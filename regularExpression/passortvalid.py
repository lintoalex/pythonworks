
from re import fullmatch

passport_no=input("enter your passport")

pattern="[A-Z][1-9][0-9][0\\s][0-9]{4}[1-9]"

matcher=fullmatch(pattern,passport_no)

print("invalid" if matcher == None else "valid")