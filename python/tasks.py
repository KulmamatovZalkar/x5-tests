# 1) Напишите функцию которая вставляет переданную переменную в строку

# def inserter(lang):
#   initial_string = 'Best language is'
#   return f'{initial_string} {str(lang)}'

# print(inserter("JS"))
# print(inserter("Basic"))

# 2) Напишите пример лямбда-функции
# ...
# initial_string = 'Best language is'
# f = lambda lang: f'{initial_string} {str(lang)}'
# print(f("Basic"))


# 3) Дан файл file.txt. В файле, условно, строка 'JavaScript'. Напишите функцию которая перепишет строку 'JavaScript' на строку 'Python'

# import os

# def rewrite(filepath):
#     path = f'{os.getcwd()}/{filepath}'
#     with open(path) as f:
#         text = f.read()
#         text.rstrip()
#         text = text.replace("JavaScript", "Python")
#         print(text)
#     f.close()


# rewrite('file.txt')
