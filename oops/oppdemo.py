class student:

    name:str

    course:int

    age:str

    gender:str

    address:str

    rollno:int



    def __init__(self,name,course,age,gender,address,rollno):

     self.name=name

     self.course=course

     self.age=age

     self.gender=gender

     self.address=address

     self.rollno=rollno

    def display_student(self):

        print(self.name,self.course,self.age,self.gender,self.address,self.rollno)

# creating

student_instance=student("hari","python",24,"male","ernakulam","13")

student_instance.display_student()