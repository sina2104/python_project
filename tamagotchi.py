from random import randrange

from animal import Animal


class Play(Animal):
    """
        our_animal - наше животное
    """
    from time import sleep

    def __init__(self):
        super().__init__()
    print("choose your animal \
                1-cat \
                2-dog")
    while True:
        try:
            pet = int(input())
            types = {1: Animal.Cat, 2: Animal.Dog}
            our_animal = types[pet]
            our_animal()
            break
        except KeyError:
            print("choose again:")
        except ValueError:
            print("choose again:")
    while True:
        our_animal.pet.clock_tick()
        print(our_animal.pet, '\n' + our_animal.pet.sounds[0])
        sleep(3)
        if our_animal.pet.mood() == 'dead':
            print('You had to care about me...')
            print(our_animal.pet.dead_look)
            break
        if our_animal.pet.mood() == 'hungry':
            food = input()
            if food in our_animal.pet.diet:
                our_animal.pet.feed()
        elif our_animal.pet.mood() == 'bored':
            entertain = input()
            our_animal.pet.teach(entertain)
            print(our_animal.pet.sounds[randrange(1, len(our_animal.pet.sounds))])


tamagotchi = Play()
