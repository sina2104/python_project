from random import randrange


class Pet:
     """
    boredom_decrement - насколько уменьшаем скучность
    hunger_decrement - насколько умеьшаем голод
    boredom_threshold - порог скучности
    hunger_threshold - порог голода
    sounds - звуки
    diet - рацион
    look - портрет
    name - имя
    hunger - счётчик голодности
    boredom -счётчик скучности
    """:
    boredom_decrement = 3
    hunger_decrement = 5
    boredom_threshold = 20
    hunger_threshold = 20
    sounds = []

    def __init__(self):
        self.diet = []
        self.look = str()
        self.name = str()
        self.hunger = max(18, randrange(self.hunger_threshold))
        self.boredom = max(15, randrange(self.boredom_threshold))
        self.sounds = self.sounds[:]

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "I feel " + self.mood() + "."
        return state

    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom()

    def feed(self):
        self.reduce_hunger()
        print("Yummy")

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)

