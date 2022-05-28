class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.tracks = tracks
        self.score = score
        self.age = age


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Mark")
Bob.change_age(34)
Bob.add_track["FE","BE", "CE"]
Bob.get_score()
