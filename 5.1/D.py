class Programmer:
    def __init__(self, name, grade, time=0):
        self.grades = ["Junior", "Middle", "Senior"]
        self.incomes = {"Junior": 10, "Middle": 15, "Senior": 20}
        self.name = name
        self.income = self.incomes[grade]
        self.hours = time
        self.grade = grade
        self.money = 0

    def work(self, time):
        self.money += time * self.income
        self.hours += time

    def rise(self):
        if self.grade == self.grades[-1]:
            self.income += 1
        else:
            self.grade = self.grades[self.grades.index(self.grade) + 1]
            self.income = self.incomes[self.grade]

    def info(self):
        return f"{self.name} {self.hours}ч. {self.money}тгр."


programmer = Programmer("Васильев Иван", "Junior")
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
