mobile={"name":"motoedge14","brand":"motoral","price":88000,"is_available":True,"offer":4300}


mobile["offer"]=500

print(mobile)


# selling offer check

if "offer" in mobile:

    selling_price=mobile.get("price")-mobile.get("offer")

    print(selling_price)

else:

    selling_price=mobile.get("prince")

    print(selling_price)
 