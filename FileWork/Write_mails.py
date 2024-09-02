 
email_ids=[
    "sam@gmail.com",
    "smith@gmail.com",
    "jhon@gmail.com",
    "stuart@gmail.com",
    "james@gmail.com",
]

f=open("C:\\Users\\linto\\OneDrive\\Desktop\\PythonJuneWorks\\FileWork\\email_id.txt","w")

for email in email_ids:

    f.write(email+"\n")