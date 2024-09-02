
placement={"python":40,"Django":34,"testing":35,"java":56,"bigdata":23}

def  get_value(key):

    return placement.get(key)

srt=sorted(placement,key=get_value,reverse=True)

print(srt)