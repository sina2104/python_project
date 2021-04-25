from animal import Cat, Dog

from time import sleep

from random import randrange


class Play(Cat, Dog):
    """
        pet - выбранное животное
        types - виды животных
        our_animal - наше животное
        three_second - 3 секунды
        first_element - первый элемент
        input_errors - ошибки ввода
    """
    three_second = 3
    first_element = 0
    input_errors = KeyError, ValueError

    def __init__(self):
        super().__init__()

    print("choose your animal: 1-cat  2-dog")
    while True:
        try:
            pet = int(input())
            types = {1: Cat, 2: Dog}
            our_animal = types[pet]
            break
        except input_errors:
            print("choose again:")
    while True:
        our_animal.pet.clock_tick()
        print(our_animal.pet, '\n' + our_animal.pet.sounds[first_element])
        sleep(three_second)
        if our_animal.pet.get_mood() == 'dead':
            print('You had to care about me...')
            print(our_animal.pet.dead_look)
            break
        if our_animal.pet.get_mood() == 'hungry':
            food = input()
            if food in our_animal.pet.diet:
                our_animal.pet.feed()
        elif our_animal.pet.get_mood() == 'bored':
            entertain = input()
            our_animal.pet.teach(entertain)
            print(our_animal.pet.sounds[randrange(first_element + 1, len(our_animal.pet.sounds))])


tamagotchi = Play()
