class Restaurant:

    hotel=str

    name=str

    price=int

    def __init__(self,name,price):

        self.name=name

        self.price=price

    def __str__(self):

        return self.name
    
class Hotel:

    def __init__(self,name,place):

        self.name=name

        self.place=place

        self.foods=[]

    def add_item(self,food):

        self.foods.append(food)

    def list_items(self):

        for f in self.foods:

            print(f)

biriyani_instance=Restaurant("biriyani",210)

poratta_instance=Restaurant("porotta",290)

chappathi_instance=Restaurant("chappathi",200)

hotel_instance=Hotel("malabar","kakkanad")

hotel_instance.add_item(biriyani_instance)

hotel_instance.add_item(poratta_instance)

hotel_instance.add_item(chappathi_instance)

hotel_instance.list_items()


