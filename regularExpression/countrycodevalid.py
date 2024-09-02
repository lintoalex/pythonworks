
# contry code match check

from re import fullmatch

text=input("enter code")

pattern="(91)\\s?[6-9]\\d{9}"

matcher=fullmatch(pattern,text)

print("invalid" if matcher == None else "valid")