#alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

print('Task 01, 02, 03')
copy_of_alice_in_wonderland = '''
"Would you tell me, please, which way I ought to go from here?"\n
"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where —— " said Alice.\n
"Then it doesn't matter which way you go," said the Cat.\n" —— so long as I get somewhere," Alice added as an explanation.\n
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."
'''
#task 02 нічого не екранував. Певно через '''
print(copy_of_alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
print('Task 04')
black_sea_area = 436402
azov_sea_area = 37800
ua_sea_area = black_sea_area + azov_sea_area
print(f'Black sea area: {black_sea_area} km^2, Azov sea area: {azov_sea_area} km^2. All UA sea area: {ua_sea_area} km^2.')

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
print('\nTask 05')
all_warehouses_product_count = 375291
WH1_and_WH2_count = 250449 # На першому і другому разом
WH2_and_WH3_count = 222950 # На другому і третьому разом

WH3_product_count = all_warehouses_product_count - WH1_and_WH2_count # Третій склад
WH1_product_count = all_warehouses_product_count - WH2_and_WH3_count # Перший склад

WH1_and_WH3_count = WH1_product_count + WH3_product_count # На першому і третьому разом

WH2_product_count = all_warehouses_product_count - WH1_and_WH3_count # Другий склад

print(f'''First WH have {WH1_product_count} products, 
second WH have {WH2_product_count} products,
third WH have {WH3_product_count} products.''')

#тут перевіримо всі товари з задачі і суму по всім складам з обчислень
all_calculated = WH1_product_count + WH2_product_count + WH3_product_count
if all_calculated == all_warehouses_product_count:
    print(True)

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
print('\nTask 06')
monthly_payment = 1179
total_payment_period = 18 #місяці
pc_price = monthly_payment * total_payment_period
print(f'''If your monthly payment is {monthly_payment}, 
and you are going to pay {total_payment_period} months, 
total price for Mike PC will be {pc_price} UAH. 
''')

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print('\nTask 07')
print(f'''
Знайди остачу від діленя чисел:
a) 8019 : 8 = {8019 % 8}    d) 7248 : 6 = {7248 % 6}
b) 9907 : 9 = {9907 % 9}    e) 7128 : 5 = {7128 % 5}
c) 2789 : 5 = {2789 % 5}    f) 19224 : 9 = {19224 % 9}
''')

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
print('\nTask 08')
print(f'''
Назва товару    Кількість   Ціна        Всього
Піца велика     4           274 грн     {(big_pizza := 4 * 274)} грн
Піца середня    2           218 грн     {(medium_pizza := 2 * 218)} грн
Сік             4           35 грн      {(juice := 4 * 35)} грн
Торт            1           350 грн     {(cake := 350)} грн
Вода            3           21 грн      {(water := 3 * 21)} грн
Тому повна ціна вийде {big_pizza + medium_pizza + juice + cake + water} грн
''')

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
print('\nTask 09')
all_photo = 232
one_page_photo = 8
pages = all_photo / one_page_photo
if 0 == all_photo % one_page_photo:
    print(f'Ihor needs {int(pages)} pages')
else:
    print(f'Ihor needs {int(pages)+1} pages')
#написав так, бо якщо просто в інт обгорнути ти б сказав "а раптом там 29.1 сторінки а ми бачимо 29". може і легше можна

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
print('\nTask 10')
distance = 1600
fuel_consump = 9 / 100
tank = 48
#1
all_fuel = fuel_consump * 1600
print(f'Скільки літрів бензину знадобиться для такої подорожі: {all_fuel}')
#2
distance_in_one_tank = tank / fuel_consump
stops_count = distance / distance_in_one_tank
print(f'Мінімум зупинок: {int(stops_count)}')

