cat1 = {
    'name': 'Spike',
    'age': 2,
    'hair_color': 'orange'

}

cat2 = {
    'name': 'Tiger',
    'age': 2,
    'hair_color': 'striped'

}

cat3 = {
    'name': 'Lucy',
    'age': 2,
    'hair_color': 'calico'

}

class Cat:
    all_cats = []
    def __init__(self, name, age, hair_color):
        self.name = name
        self.age = age
        self.hair_color = hair_color
        self.cute = True
        Cat.all_cats.append(self)

    def meow(self):
        print(f"Meeeeeeow my name is {self.name}")
        return self
    
    def play(self):
        print(f"I'm playing with a ball of yarn")
        return self

    def __repr__(self):
        return f"Cat Object Name:{self.name} Age:{self.age}"

    
    

cat1 = Cat("Spike", 2, 'orange')
cat2 = Cat("Tiger", 2, "striped")
cat3 = Cat("Lucy", 2, 'calico')

# print(cat1.name)
print(Cat.all_cats)

# cat1.new_attribute = 73
# print(cat1.new_attribute)
# print(cat2.new_attribute)

# cat1.meow().play().meow().play()

# print(type(cat1))

print(cat1)