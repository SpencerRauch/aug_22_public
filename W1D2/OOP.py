cat_dict1 = {
    'name': 'Spike',
    'age': 2,
    'hair_color': 'orange'

}

cat_dict2 = {
    'name': 'Tiger',
    'age': 2,
    'hair_color': 'striped'
}
cat_dict3 = {
    'name': 'Lucy',
    'age': 2,
    'hair_color': 'calico'
}

list_of_dictionaries = [cat_dict1,cat_dict2,cat_dict3]
class Toy:
    def __init__(self, type, color, action):
        self.type = type
        self.color = color
        self.action = action

class Cat:
    all_cats = []
    def __init__(self, data):
        self.name = data['name']
        self.age = data['age']
        self.hair_color = data['hair_color']
        self.cute = True
        self.toy = None
        Cat.all_cats.append(self)
    
    @classmethod
    def print_all_cats(cls):
        for one_cat in cls.all_cats:
            print(f"Name: {one_cat.name} Age: {one_cat.age} Hair-color: {one_cat.hair_color}")

    def meow(self):
        print(f"Meeeeeeow my name is {self.name}")
        return self
    
    def play(self):
        print(f"{self.name} plays with {self.toy.color} {self.toy.type} and it {self.toy.action}")
        return self

    def __repr__(self):
        return f"Cat Object Name:{self.name} Age:{self.age}"

    @staticmethod
    def convert_years_to_cat_years(years):
        return years * 7


    
        
toy1 = Toy("ball of yarn", "red", "rolls aways and unravels")
toy2 = Toy("scratcher", "blue", "takes critical damages")
toy3 = Toy("laser pointer", "red", "jumps around the room")


# cat1 = Cat("Spike", 2, 'orange', "ball of yarn", "red", "rolls aways and unravels")
# cat1 = Cat(cat_dict1)
# cat2 = Cat(cat_dict2)
# cat3 = Cat(cat_dict3)

# cat2.toy = toy1
list_of_instances = []
for cat_dict in list_of_dictionaries:
    this_cat = Cat(cat_dict)
    list_of_instances.append(this_cat)

print(list_of_instances)


# cat1.play()
# print(cat1.name)
# print(Cat.all_cats)
# Cat.all_cats[0].play()

# cat1.new_attribute = 73
# print(cat1.new_attribute)
# print(cat2.new_attribute)

# cat1.meow().play().meow().play()

# print(type(cat1))

# print(cat1)
# my_age = 34
# print(Cat.convert_years_to_cat_years(my_age))
# Cat.print_all_cats()