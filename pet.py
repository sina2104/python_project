from random import randrange


class Pet:
    """
        boredom_decrement - насколько уменьшаем скучность
        hunger_decrement - насколько умеьшаем голод
        common_hunger - вероятное значение голода
        common_boredom - вероятное значение скучности
        boredom_threshold - порог скучности
        hunger_threshold - порог голода
        death_threshold - порог смерти
        sounds - звуки
        diet - рацион
        look - портрет
        dead_look - животное умер
        name - имя
        hunger - счётчик голодности
        boredom -счётчик скучности
        first_element - первый элемент
        number - номер состояния
    """
    boredom_decrement = 3
    hunger_decrement = 5
    common_hunger = 21
    common_boredom = 21
    boredom_threshold = 20
    hunger_threshold = 20
    death_threshold = 25
    first_element = 0

    def __init__(self):
        self.diet = []
        self.look = ''
        self.dead_look = ''
        self.name = ''
        self.hunger = max(self.common_hunger, randrange(self.hunger_threshold))
        self.boredom = max(self.common_boredom, randrange(self.boredom_threshold))
        self.sounds = []

    def __str__(self):
        state = f"I feel {self.get_mood(1)[0]}."
        return state

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def get_mood(self, number):
        if self.hunger > self.death_threshold and number == 0:
            return "dead"
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold and number == 1:
            return "happy"
        if self.hunger > self.hunger_threshold and number == 2:
            return "hungry"
        if self.boredom > self.boredom_threshold and number == 3:
            return "bored"
        else:
            return "none"

    def happy_mode(self, our_animal):
        return "happy"

    def dead_mode(self, our_animal):
        if our_animal.pet.get_mood(0) == 'dead':
            print('You had to care about me...')
            print(our_animal.pet.dead_look)
            return True
        return "dead"

    def hungry_mode(self, our_animal):
        if our_animal.pet.get_mood(2) in ['hungry', ["bored", "hungry"]]:
            print("feed me please:")
            food = input()
            if food in our_animal.pet.diet:
                our_animal.pet.feed()

    def bored_mode(self, our_animal):
        if our_animal.pet.get_mood(3) in ['bored', ["bored", "hungry"]]:
            print("teach me something please:")
            first_element = 0
            entertain = input()
            our_animal.pet.teach(entertain)
            print(our_animal.pet.sounds[randrange(first_element + 1, len(our_animal.pet.sounds))])

    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom()

    def feed(self):
        self.reduce_hunger()
        print("Yummy")

    def reduce_hunger(self):
        self.hunger = max(self.first_element, self.hunger - self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom = max(self.first_element, self.boredom - self.boredom_decrement)
