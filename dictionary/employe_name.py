
employe={"name":"hari","dept":"r&d","salary":50000,"combo_offer":1000,"extra_working_day":2}

for k,v in employe.items():

    if "extra_working_day" in employe:

        net_pay=employe.get("salary")+employe.get("combo_offer")*employe.get("extra_working_day")

    else:
      
      net_pay=employe.get("salsry")

print(net_pay)