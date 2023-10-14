import re

# Напишите скрипт, который извлекает все хештеги (например, #python)
# из данного текста. Вы можете использовать регулярные выражения,
# чтобы найти все вхождения хештегов.


text_1 = ''' Хеште́г[1], также хэште́г (англ. hashtag от hash — знак решётки (#) и tag — метка) ####
ключевое слово, тема или несколько слов сообщения, тег (пометка), используемый в микроблогах и 
социальных сетях, облегчающий поиск сообщений по теме или содержанию и начинающийся со знака решётки.
Представляет собой слово или объединение слов (без пробелов), которому предшествует символ #,
например: #искусство, #техника, #биткойн. Хештеги используют в рекламной продукции или арт-представлениях
в качестве отсылки к появившейся тен#денции  интернете  или в попытке создать такую тенденцию. 
тен#денции, 77733#122, 85@$#$,  @#$@##$@1232, ,,,...#'',,,
'''

my_re = r'[^\w]#\w+[^\W]'
print(re.findall(my_re, text_1))


# Откройте текстовый файл для чтения.Прочитайте содержимое файла и сохраните
# его в строковой переменной.Напишите регулярное выражение, которое ищет и
# извлекает электронные адреса из текста.Используйте модуль re для выполнения
# поиска с помощью регулярного выражения.Сохраните найденные адреса в отдельный
# файл или выведите их на экран.

re_email = r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)'


with open('info.txt', 'r') as read_fp:
    new_text = read_fp.read()
    result = re.findall(re_email, new_text)
    print(result)
