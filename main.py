class Puppy:
    def __init__(self, name, breed):
        self.name = name
        self.age = 0.2
        self.breed = breed

    def __str__(self):
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