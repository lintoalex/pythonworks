
from re import fullmatch

text="KL-08-BN-4970"

pattern="(KL)(-)?[0-9]{2}(-)?[A-Z]{1,2}(-)?[0-9]{4}"

matcher=fullmatch(pattern,text)

print("invalid" if matcher == None else "valid")

#----------------------------------------------------------------------------------------------------------------------------

text="KL08BN4970"

pattern="(KL)[0-9]{2}[A-Z]{1,2}[0-9]{4}"

matcher=fullmatch(pattern,text)

print("invalid" if matcher == None else "valid")

#----------------------------------------------------------------------------------------------------------------------------

text=input("enter number")

pattern="(KL)(-)?[0-9]{2}(-)?[A-Z]{1,2}(-)?[0-9]{4}"

matcher=fullmatch(pattern,text)

print("invalid" if matcher == None else "valid")
