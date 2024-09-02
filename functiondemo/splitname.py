email_id="vipin@gmail.com"

at_indx_pos=email_id.index("@")

user_name=email_id[:at_indx_pos]

print(user_name)

domain=email_id[at_indx_pos:]

print(domain)