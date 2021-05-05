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
    """
    boredom_decrement = 3
    hunger_decrement = 5
    common_hunger = 18
    common_boredom = 15
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

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def get_mood(self):
        if self.hunger > self.death_threshold:
            return "dead"
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "hungry"
        elif self.hunger <= self.hunger_threshold and self.boredom > self.boredom_threshold:
            return "bored"
        else:
            return "hungry and board"

    def __str__(self):
        state = "I feel " + self.get_mood() + "."
        return state

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
