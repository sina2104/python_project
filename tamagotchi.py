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
        number - номер состояния
        modes - состояния животное
        mode_commands - комманды в соответствии с состоянием животного
        feelings - состояния животного, о которых мы сообщаем хозяину
        commands - комманды
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
    commands = {
        'our_animal.pet.happy_mode(our_animal)': our_animal.pet.happy_mode,
        'our_animal.pet.hungry_mode(our_animal)': our_animal.pet.hungry_mode,
        'our_animal.pet.bored_mode(our_animal)': our_animal.pet.bored_mode
    }
    while our_animal.pet.dead_mode(our_animal) != "daed":
        modes_command = []
        modes = []
        number = 0
        while number <= 3:
            if our_animal.pet.get_mood(number) != "none":
                modes.append(our_animal.pet.get_mood(number))
            number += 1
        feelings = modes[first_element]
        our_animal.pet.clock_tick()
        for i in range(len(modes)):
            modes_command.append(f"our_animal.pet.{modes[i]}_mode(our_animal)")
            if i != 0:
                feelings += f" and {modes[i]}"
        print(f"I feel {feelings}!")
        sleep(three_second)
        for el in modes_command:
            commands[el](our_animal)


tamagotchi = Play()
