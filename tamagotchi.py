from random import randrange
from animal import Animal


class Play(Animal):
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
            play1 = types[pet]
            play1()
            break
        except KeyError:
            print("choose again:")
        except ValueError:
            print("choose again:")
    while 1:
        play1.pet.clock_tick()
        print(play1.pet, '\n' + play1.pet.sounds[0])
        sleep(3)
        if play1.pet.mood() == 'dead':
            print('You had to care about me...')
            print(play1.pet.dead_look)
            break
        if play1.pet.mood() == 'hungry':
            food = input()
            if food in play1.pet.diet:
                play1.pet.feed()
        elif play1.pet.mood() == 'bored':
            entertain = input()
            play1.pet.teach(entertain)
            print(play1.pet.sounds[randrange(1, len(play1.pet.sounds))])


tamagotchi = Play()
