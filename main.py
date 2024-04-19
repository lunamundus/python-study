class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def sleep(self):
        print("Zzz...")

class GuardDog(Dog):
    def __init__(self, name, breed):
        super().__init__(name=name, breed=breed, age=5)         # super()는 부모 class를 참조 -> 부모 class인 Dog의 __init__() 메서드를 호출함
        self.aggresive = True                                   # 부모 class에 없는 Property도 가질 수 있음
    
    def rrrrr(self):
        print("Stay Away!!")

class Puppy(Dog):
    def __init__(self, name, breed):
        super().__init__(name=name, breed=breed, age=0.1)       # super()는 부모 class를 참조 -> 부모 class인 Dog의 __init__() 메서드를 호출함
        self.spoiled = True                                     # 부모 class에 없는 Property도 가질 수 있음

    def woof_woof(self):
        print("Woof Woof!")


ruffus = Puppy(
    name="Ruffus", 
    breed="Beagle"
)

bibi = GuardDog(
    name="Bibi",
    breed="Dalmatian"
)

ruffus.sleep()
bibi.sleep()