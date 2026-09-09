names = ["atif"  , 'ali' , 'usman'] 
age = (20, 25, )

# numbers = [10, 15, 20, 25, 30, 35, 40]
# dictonary 
# user  = {
#     "name" : "atif" ,
#     "age" : 20 ,
#     'city' : "Mumbai" , 
#     'country' : "India"

# }
# result = [num for num in numbers if num % 2 !=0 if num > 10 if num < 40]
# for num in result : 
#     print(num) ;
# for key in user : 
#     print(f"{key} : {user[key]}") ;

# for i , number in enumerate(numbers) : 
#     print(i , number) ; 

# print(any(num % 2 == 0 for num in numbers))

# print(f"length of names : {len(names)}")
# print(max(names))
# for name , age in zip(names , age) :
#     print(f"Name : {name} , Age : {age}")

# text = "python is easy and python is powerful"

# words = text.split(" ")
# freq = {

# }

# for word in words : 
#     if word in freq : 
#         freq[word] += 1
#     else : 
#         freq[word] = 1 
# print(freq)


# students = {
#     "student1": {
#         "name": "Atif",
#         "marks": 85
#     },
#     "student2": {
#         "name": "Ali",
#         "marks": 100
#     },
#     "student3": {
#         "name": "Ahmed",
#         "marks": 91
#     }
# }

# print(max(students))


numbers = range(1, 21)

res  = [num ** 2 for num in numbers if num % 2 == 0 ]

print(res)

      