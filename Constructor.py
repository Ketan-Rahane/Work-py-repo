
class Student:
    def __init__(self, name, roll, subjects):
        self.name = name
        self.roll = roll
        self.subjects = subjects  # Creating Dictionary of subjects and marks

    def display_percentage(self):
        total = sum(self.subjects.values())
        percentage = total / len(self.subjects)
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Percentage:", percentage, "%")


subjects = {
    "Math": 85,
    "Science": 90,
    "English": 80,
    "History": 75,
    "Marathi": 95
}

s1 = Student("Jay", 21, subjects)
s1.display_percentage()
