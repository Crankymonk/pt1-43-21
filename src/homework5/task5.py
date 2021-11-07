'''
5. Языки
Каждый из N школьников некоторой школы знает Mi языков. Определите,
какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
Входные данные
Первая строка входных данных содержит количество школьников N.
Далее идет N чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков,
которые знает i-й школьник.
Пример входных данных:
3          # N количество школьников
2          # M1 количество языков первого школьника
Russian    # языки первого школьника
English
3          # M2 количество языков второго школьника
Russian
Belarusian
English
3
Russian
Italian
French

Выходные данные
В первой строке выведите количество языков, которые знают все школьники.
Начиная со второй строки - список таких языков. Затем - количество языков,
которые знает хотя бы один школьник, на следующих строках - список таких языков.
'''


N = int(input('Введите количество школьников: '))
language_pool = set()
list_lang = list()

for i in range(N):
    M = int(input('Введите количество языков, которые знает школьник: '))
    language = ''
    for i in range(M):
        language = input('Введи язык: ')
        list_lang.append(language)

language_pool = set(list_lang)  # Языки, которые знает хотя бы один школьник
common_languages = list()

for lang in list_lang:
    if list_lang.count(lang) == N and lang not in common_languages:
        common_languages.append(lang)  # Создаем список общих языков для всех

print(len(common_languages))
print('\n'.join(common_languages))  # Выводим общие языки с новой строки
print(len(language_pool))
print('\n'.join(language_pool))  # Выводим все известные языки с новой строки