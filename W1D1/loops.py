#LOOPS

#FOR LOOPS

"""
for ___ in ___:
    pass

blank #1: iterative variable
blank #2: the data we're iterating over / loop through

Range: start (optional, default 0), stop (required EXCLUSIVE), step(optional, default 1)

"""
stop = 50
# for x in range(1,stop+1):
#     print(x)

list = ['pineapple','strawberry','mango','lychee','guanabana','papaya']
#Looping over a List
# for fruit in list:
#     print(fruit)
#when iterating over a list, the iterative variable represents each element in turn

# for index in range(len(list)):
#     print(f"before the continue {index}")
#     if index == 2:
#         break
#     print(list[index])

list2 = [ {
    'calories': 100,
    'name': 'meatloaf',
    'carbs': 'a lot',
    'vegan': False
},
{
    'calories': 50,
    'name': 'strawberry',
    'carbs': 'a bit',
    'vegan': True
}]

# # iterating over a dictionary, IV is the keys 
# for key in food:
#     print(key)
#     print(food[key])

# for food_dict in list2:
#     for key in food_dict:
#         print(f'{key}: {food_dict[key]}')

#string
string = "Hello"

for char in string:
    print(char)

#WHILE LOOPS

"""
while(expression):
    code needs to exist here that will break the condition

"""
y = 10
while(y>0):
    # y = y - 1
    print(y)