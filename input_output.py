"""
последовательно запрашивающую ваши фамилию, имя,
отчество ивыводящую их одной строкой в последовательности: фамилия→имя→отчество;
"""

female = input("Введите вашу фамилию: ")
print(female[-2::])
print(female[:-2])

name = input("Введите ваше имя: ")
secondname = input("Введите ваше отчество: ")
date = input("Введите день вашего рождения в формате ДД: ")
month = input("Введите месяц вашего рождения в формате ММ: ")
year = input("Введите год вашего рождения в формате ГГГГ: ")

if female[-2::] in ('ин', 'ый', 'ий', 'ой'):
    if female[-2::] in ('ый', 'ий', 'ой'):
        female = female[:-2] + "ая"
    else:
        female = female[:-2] + "яя"

# print("{} {} {}".format(female, name, secondname))
# print("{} {} {}".format(name, secondname, female+'a'))
# print("{}.{}.{}".format(date, month, year))
# print("{}/{}/{}".format(date, month, year))
# print("{}-{}-{}".format(date, month, year))
town = input("Введите город своего рождения: ")
print("Вас зовут {} {} {}, вы родились {}.{}.{}, в городе {}".format(female, name, secondname, date, month, year, town))
