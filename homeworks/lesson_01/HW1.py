# task 01 == Виправте синтаксичні помилки
print("Task 1")
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
print("Task 2")
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
print("Task 3")
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
print("Task 6")
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(perimetery)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?

"""
print("Task 7")
apples = 4
pears = apples + 5
plums =  apples - 3
all_tries = apples + pears + plums
print(all_tries)

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
print("Task 8")
first_part_of_the_day = 5
second_part_of_the_day = first_part_of_the_day - 10
last_part_of_the_day = second_part_of_the_day + 4
print(last_part_of_the_day)

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
print("Task 9")
boys = 24
girls = boys / 2
today_boys = boys - 1
today_girls = girls - 2

today_kids = today_boys + today_girls
print(today_kids)

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
print("Task 10")
first_book = 8
second_book = first_book + 2
third_book = first_book / 2 + second_book / 2
all_books = first_book + second_book + third_book
print(all_books)

# change