from pet import Pet


class Animal(Pet):
    def __init__(self):
        super().__init__()

    class cat:
        pet = Pet()
        pet.diet = ['chicken', 'turkey', 'apple']
        pet.name = 'kitty'
        pet.look = ' /\_/\ \n( o.o )\n > ^ <'
        pet.sounds.append('Mrrrr')
        print("I'm a " + pet.name, '\n' + pet.look)

    class dog:
        pet = Pet()
        pet.diet = ['beef', 'bone', 'carrot']
        pet.name = 'big dog'
        pet.look = '  /^ ^\ \n / 0 0 \ \n V\ Y /V \n  / - \ \n / | \nV__) ||'
        pet.sounds.append('Haf Haf')
        print("I'm a " + pet.name, '\n' + pet.look)
