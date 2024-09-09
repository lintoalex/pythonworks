

class operation:

    def perform_add(self,*args):


        total=0

        for arg in args:

            isinstance(arg,(int,float))

            total=total+arg

        return total
    
match=operation()

print(match.perform_add(10,20,30.5,60.2))




# class operation:

#     def perform_add(self,*args):

#         total=0

#         for arg in args:

#             isinstance(arg,(int,float))

#             total=total+arg

#         return total
    
# match=operation()

# print(match.perform_add(10,20,30.5,60.2))