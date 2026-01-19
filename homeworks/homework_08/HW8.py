# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент",
# який дозволяє змінювати середній бал студента. Виведіть інформацію про студента та змініть його середній бал.

class Student:
    def __init__(self, name, surname, age, avg_mark):
        self.name = name
        self.surname = surname
        self.age = age
        self.avg_mark = avg_mark

    def mark_correction(self, new_mark):
        self.avg_mark = new_mark

    def info(self):
        print(self.name, self.surname, self.age, self.avg_mark)


student_maks = Student('Maks', 'Grim', 20, 4.5)

student_maks.info()
student_maks.mark_correction(4.8)
student_maks.info()