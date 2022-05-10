# import pdfplumber
# from pathlib import Path

# def extract_to_txt(path):
#     path = Path(path)
#     if path.is_file():
#         with pdfplumber.PDF(open(str(path), mode="rb")) as pdf:
#             pages = pdf.pages[0]
#             pdf_text = pages.extract_text()
#         return pdf_text
#     else:
#         return f"{path} does not exist"


# def main():
#     path = input("Введите путь до вашего файла:")
#     print(extract_to_txt(path))

# if __name__ == '__main__':
#     main()


# Напишите программу для сохранения текста из PDF в TXT
# У программы должен быть интерфейс ввода пути до файла из которого необходимо достать текст

# Дополнительное задание: * Модернезируйте программу чтобы она преобразовывала полученный текст из PDF в MP3 файл и воспроизводила его голосом

# Необходимые пакеты:
# pdfplumber - работа с PDF
# * gtts - воспроизведение текстовых файлов голосом

# Можно пользоваться гуглом для чтения документации пакетов

import pdfplumber
from pathlib import Path
from gtts import gTTS

def get_text(file_path='test.pdf'):
  if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':

    with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
      pages = [page.extract_text() for page in pdf.pages]

    text = ''.join(pages)
    var = gTTS(text=text, lang='en')
    var.save('text.mp3')
    return text
      
  else:
    return 'File not exists, check the file path'

def main():
  file_path = input("\nEnter a file path:")
  print(get_text(file_path))

if __name__ == '__main__':
  main()