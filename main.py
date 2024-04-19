class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

class GuardDog(Dog):                    # GuardDog class는 Dog class를 상속받음
                                                            # -> name, breed, age를 그대로 가지게 됨
    def rrrrr(self):
        print("Stay Away!!")

class Puppy(Dog):                       # Puppy class는 Dog class를 상속받음
                                                            # -> name, breed, age를 그대로 가지게 됨
    def woof_woof(self):            # 사용하지 않더라도 메서드 내에서 self 파라미터는 꼭 받아와야 함
        print("Woof Woof!")

    def introduce(self):
        self.woof_woof()            # 메서드 내에서 다른 메서드를 호출할 수 있음
        print(f"My name is {self.name} and I am a baby {self.breed}.")
        self.woof_woof()


ruffus = Puppy(
    name="Ruffus", 
    breed="Beagle"
)

bibi = Puppy(
    name="Bibi",
    breed="Dalmatian"
)

ruffus.introduce()