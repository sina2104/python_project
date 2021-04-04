from random import randrange
from pet import Pet
from animal import Animal

class Play(Animal):
    from time import time, sleep

    def __init__(self):
        super().__init__()
    play1 = Animal
    print("choose your animal \
        1-cat \
        2-dog")
    pet = int(input())
    if pet == 1:
        play1 = play1.cat
        play1()
    if pet == 2:
        play1 = play1.dog
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
