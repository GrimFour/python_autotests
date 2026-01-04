adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print(f'\nTask 1-3')
#adwentures_of_tom_sawer = adwentures_of_tom_sawer.split()
# print(adwentures_of_tom_sawer_sentences.split())
adwentures_of_tom_sawer = ' '.join(adwentures_of_tom_sawer.split())
print(adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print(f'\nTask 4')
count_of_h = adwentures_of_tom_sawer.count('h')
print(count_of_h)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print(f'\nTask 5')
count_of_capital = sum(1 for word in adwentures_of_tom_sawer.split() if word[0].isupper())
print(count_of_capital)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print(f'\nTask 6')
word = 'Tom'
first = adwentures_of_tom_sawer.find(word)
second = adwentures_of_tom_sawer.find(word, first + len(word))
print(second)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
print(f'\nTask 7')
adwentures_of_tom_sawer_sentences = None
adwentures_of_tom_sawer_sentences = [s.strip() for s in adwentures_of_tom_sawer.split('.') if s.strip()]
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print(f'\nTask 8')
#print(adwentures_of_tom_sawer_sentences[3])
adwentures_of_tom_sawer_fourth_sentences = adwentures_of_tom_sawer_sentences[3]
adwentures_of_tom_sawer_fourth_sentences = adwentures_of_tom_sawer_fourth_sentences.lower()
print(adwentures_of_tom_sawer_fourth_sentences)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print(f'\nTask 9')
fraze = "By the time"
start_with_fraze = [s for s in adwentures_of_tom_sawer_sentences if s.startswith(fraze)]
print(start_with_fraze)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print(f'\nTask 10')
last_sentence = adwentures_of_tom_sawer_sentences[-1]
word_count = len(last_sentence.split())
print(word_count)