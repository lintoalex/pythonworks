class person:
    
    def __init__(self,name,age,gender):

        self.name=name

        self.age=age

        self.gender=gender

    def display(self):

        print(self.name,self.age,self.gender)  

class employe(person):

    def __init__(self,name,age,gender,eid,department,salary):
        
        super().__init__(name,age,gender)

        self.eid=eid

        self.department=department

        self.salary=salary

    def display(self):

        super().display()

        print(self.eid,self.department,self.salary)

emp_instance=employe("vipin",30,"male","e01","civil",20000)

emp_instance.display()
