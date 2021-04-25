from pet import Pet
"""
    тут мы определяем вид животного
"""


class Cat(Pet):
    def __init__(self):      
        super().__init__()
    pet = Pet()
    pet.diet = ['chicken', 'turkey', 'apple']
    pet.name = 'kitty'
    pet.look = '''
     /\_/\ 
    ( o.o )
     > ^ <'''
    pet.dead_look = '''
     /\_/\ 
    ( *.* )
     > ^ < '''
    pet.sounds.append('Mrrrr')
    print(f"I'm a {pet.name}{pet.look}")


class Dog(Pet):
    def __init__(self):   
        super().__init__()
    pet = Pet()
    pet.diet = ['beef', 'bone', 'carrot']
    pet.name = 'big dog'
    pet.look = '''
     /^ ^\ 
    / 0 0 \ 
    V\ Y /V 
     / - \ 
    /    |
    V__) ||'''
    pet.dead_look = '''  
     /^ ^\  
    / * * \ 
    V\ Y /V 
     / - \ 
    /    | 
    V__) ||'''
    pet.sounds.append('Haf Haf')
    print(f"I'm a {pet.name}{pet.look}")
