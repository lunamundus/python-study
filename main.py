class Puppy:
    def __init__(self, name, breed): # 파라미터를 정의하여 객체 생성 시 데이터를 받아올 수 있음
        self.name = name
        self.age = 0.2
        self.breed = breed

    def __str__(self):
        # self 객체를 이용하여 같은 class 내에서 데이터를 사용할 수 있음 -> 같은 메모리 주소를 참조하고 있기 때문
        return f"name: {self.name}, breed: {self.breed}"


ruffus = Puppy(
    name="Ruffus", 
    breed="Beagle"
)

bibi = Puppy(
    name="Bibi",
    breed="Dalmatian"
)

print(ruffus)