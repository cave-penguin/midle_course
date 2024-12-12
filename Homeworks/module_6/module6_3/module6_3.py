from random import randint


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        self._cords[0] += self.speed * dx
        self._cords[1] += self.speed * dy
        if self.speed * dz < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[2] += self.speed * dz

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: '
              f'{self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print(f"Here are(is) {randint(1, 4)} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    # def __init__(self, _cords):
    #     super().__init__(_cords)

    def dive_in(self, dz):
        self._cords[2] -= int((self.speed / 2 * abs(dz)))


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    sound = "Click-click-click"
    
    def __init__(self, speed):
        super().__init__(speed)
    


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
