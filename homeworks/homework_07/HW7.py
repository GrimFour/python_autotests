# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
print(f'\nTask 1')
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier * number <= 25:
        result = multiplier * number
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        # result = number * multiplier
        # # десь тут помила, а може не одна
        # if  result > 25:
        #     # Enter the action to take if the result is greater than 25
        #     pass
        # print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
print(f'\nTask 2')
def plus (first_number: int, second_number: int) -> int:
    print(f'{first_number} + {second_number} = {first_number + second_number}')

plus(5, 2)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
print(f'\nTask 3')

def avarage_func(some_list: list):
    sum = 0
    for number in some_list:
        sum += number
    result = sum / len(some_list)
    print(result)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
avarage_func(my_list)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
print(f'\nTask 4')

def reverse_string(s: str) -> str:
    return s[::-1]

print(reverse_string('Hello, world!'))
#даров, Олег

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
print(f'\nTask 5')

def longest_word(list_of_words: list) -> str:
    return max(list_of_words, key=len, default=None)

some_list = ['Мені', 'тринадцятий', 'минало', 'я', 'пас', 'ягнята', 'за', 'селом']
print(longest_word(some_list))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
print(f'\nTask 6')

def find_substring(str1, str2):
    if str2 == "":
        return 0

    for i in range(len(str1) - len(str2) + 1):
        if str1[i:i + len(str2)] == str2:
            return i
    return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# домашка 1 таска 8
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
print(f'\nTask 7')

# first_part_of_the_day = 5
# second_part_of_the_day = first_part_of_the_day - 10
# last_part_of_the_day = second_part_of_the_day + 4
# print(last_part_of_the_day)

def final_temperature(first_part_of_the_day: int, second_part_of_the_day: int, third_part_of_the_day: int) -> int:
    temperature = first_part_of_the_day + second_part_of_the_day + third_part_of_the_day
    return temperature

print(final_temperature(5, -10, 4))

# task 8
# домашка 1 таска 6 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
print(f'\nTask 8')
# perimetery = storona_1 + storona_2 + storona_3 + storona_4
# print(perimetery)

def perimeter(first_side: int, second_side: int, third_side: int, fourth_side: int) -> int:
    return first_side + second_side + third_side + fourth_side

print(perimeter(5, 4, 4, 5))

# task 9
# Буде рекорд_свапер як в домашці 5_2, таска друга.
print(f'\nTask 9')

list_task9 = ['Мені', 'тринадцятий', 'минало', 'я', 'пас', 'ягнята', 'за', 'селом']

def recordswaper (some_list: list, first_index: int, second_index: int):
    some_list[first_index], some_list[second_index] = some_list[second_index], some_list[first_index]
    print(some_list)

recordswaper(list_task9, 2, 6)

# task 10
# З домашки 6_1
# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

# user_text = input('Type ur text pls: ')
# print(len(set(user_text)) > 10)
print(f'\nTask 10')

def has_more_than_10_unique_chars(text: str) -> bool:
    return len(set(text)) > 10

print(has_more_than_10_unique_chars('тринадцятий'))
print(has_more_than_10_unique_chars('тринадцятий минало'))

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""