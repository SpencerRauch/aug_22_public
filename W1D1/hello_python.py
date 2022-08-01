print('Hello')

x=4
name_of_variable = "snake case"

# DATA TYPES

#Primitive 
"""
strings "strings of text"
booleans True or False
numbers 
"""
bool = True
number = 9
num2 = 9.3


#Composite

# tuples - immutable list of elements
tuple = ('str1', 'str2', 'str3')

# tuple[2] = "Bob" THIS CREATES AN ERROR CANNOT DO
# print(tuple[2])

#list -- called array in js
list = [1,2,3,4,5,6]
#zero - indexed
#assignment
list[3] = 9
last_item = list[5]
# print(last_item)

#split operator
new_list = list[-3:]
# print(new_list)
string = "abcdef"
# print(min(string))
#functions
#len() returns length of array
# print(len(new_list))
#max(), min() //return the maximum or minimum
# print(max(new_list))

#methods for lists:
#.append() it appends! adds an element
new_list.append(100)
# print(new_list)
#.sort()
new_list.sort(reverse=True)
# print(new_list)
popped = new_list.pop(2)
#pop can also take an index
# print(new_list)
# print(popped)

#dictionaries collections of elements in key value pairs
dict = {
    'key': 'values'
}

dog = {
    'age':3,
    'breed': 'corgi'
}

# print(dog['age'])
dog['name'] = "Spot"

#checking if a key exists
if "key" in dict:
    pass

if 'age' in dog:
    print(f"Dog is {dog['age']} old")

# print(dog.get('pineapple','default'))

# print(dog)

# print(len(dog))

# age = dog.pop('age') removes and stores
del dog['age'] #just removes
dog.clear()
# print(age)
# print(dog)

#Conditionals #Devin says "something that can return true or false and reacts based on the result "
#Operands: or, >, =>, <, <=, and, ==, !, not, is 
#keywords: if, else, elif

number = 70

if number > 75:
    print('big num')
elif number < 60:
    print('small num')
else:
    print("change made")









