class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def dispaly(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

s1 = Student("Muhammad Hamza Ismail", 85)
s1.dispaly()