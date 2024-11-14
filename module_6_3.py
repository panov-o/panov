from random import randint

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    cords = [0, 0, 0]

    def __init__(self, speed):
        self.speed = speed

    def move(self, dx, dy, dz):
        if dz <= 0:
            print('Здесь слишком глубоко, я не могу нырнуть.')
        else:
            self.cords = [dx, dy, dz]

    def get_cords(self):
        print(f'X: {self.cords[0] * self.speed}, Y: {self.cords[1] * self.speed}, Z: {self.cords[2] * self.speed}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print('Извини, я настроен миролюбиво :)')
        else:
            print('Будь осторожен, я нападаю на тебя 0_0')

    def speak(self):
        print(f'{self.sound}')

class Bird(Animal):
    beak = True

    # def __init__(self):

    def lay_eggs(self):
        r = randint(1,4)
        print(f'Вот {r} яйца для тебя')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self.dz = dz
        self.cords[2] -= abs(dz//2)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8
    pass

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):

    sound = "Click-click-click"


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
