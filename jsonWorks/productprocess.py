
from json import load

f=open("C:\\Users\\linto\\OneDrive\\Desktop\\PythonJuneWorks\\jsonWorks\\product.json",encoding="UTF-8")

product=load(f)


# print(len(product))

product_items=[i.get("title") for i in product]

print(product_items)


category_product=[i.get("title") for i in product if i.get("category")=="jewelery"]

# print(category_product)


product_price=[i.get("title") for i in product if i.get("price")>100]

# print(product_price)


product_range_price=[i.get("title") for i in product if i.get("price")>100 and i.get("price")<150]

# print(product_range_price)


def get_rating_count(dic):

    return dic.get("rating").get("count")

top_selling_product=max(product,key=get_rating_count)

# print(top_selling_product)
