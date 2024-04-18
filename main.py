class Puppy:
    def __init__(self):         # 모든 메서드는 self를 첫번째 파라미터로 가짐
        # class의 기본 값을 세팅
        self.name = "ruffus"
        self.age = 21
        self.breed = "Beagle"

ruffus = Puppy()                # 객체 초기화 (변수를 하나의 객체로서 선언)

print(ruffus.name, ruffus.age, ruffus.breed)