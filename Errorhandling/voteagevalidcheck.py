
def poll(age):

    if age<18:

        raise Exception("invalid age")
    
    else:

        print("vote")


try:

    poll(17)

except Exception as e:

    print(e)