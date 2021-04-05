from random import randrange
from pet import Pet
from animal import Animal

class Play(Animal):
    """
    здесь написана сама игра
    play1 - животное, с которым мы работаем
    """
    from time import time, sleep

    def __init__(self):
        super().__init__()
    play1 = Animal.Cat
    print("choose your animal \
                1-cat \
                2-dog")
    while True:
        try:
            pet = int(input())
            types = {1: Animal.Cat, 2: Animal.Dog}
            play1 = types[pet]
            break
        except KeyError:
            print("choose again:")
        except ValueError:
            print("choose again:")
    play1()
    start = time()
    while 1:
        play1.pet.clock_tick()
        print(play1.pet, '\n' + play1.pet.sounds[0])
        sleep(3)
        if play1.pet.mood() == 'hungry':
            food = input()
            if food in play1.pet.diet:
                play1.pet.feed()
        elif play1.pet.mood() == 'bored':
            entertain = input()
            play1.pet.teach(entertain)
            print(play1.pet.sounds[randrange(1, len(play1.pet.sounds))])
        if time() - start > 180:
            print(play1.pet.look)
            print("It's time to die! Goodbye!")
            break


tamagotchi = Play()
