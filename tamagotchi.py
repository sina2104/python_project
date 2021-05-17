from animal import Cat, Dog

from time import sleep


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
    while not our_animal.pet.dead_mode(our_animal):
        our_animal.pet.clock_tick()
        print(f"{our_animal.pet}\n{our_animal.pet.sounds[first_element]}")
        sleep(three_second)
        our_animal.pet.hungry_mode(our_animal)
        our_animal.pet.bored_mode(our_animal)


tamagotchi = Play()
