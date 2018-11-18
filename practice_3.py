in_str = input('Введите входную строку: ')
out_str = ''

key = int(input('Введите ключ для шифра Цезаря:'))
lang = input('Введите язык rus/eng: ')
mode = input('Выберите режим(зашифровать - crypt, дешифровать - decrypt): ')
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

in_str = in_str.lower()
mode = mode.lower()

if lang == 'eng':
    if mode == 'crypt' and in_str!='':
        for char in in_str:
            if char != ' ':
                ord_char = (ord(char)-97+key)%26 + 97
                out_str += chr(ord_char)
            else:
                out_str += ''

    elif mode == 'decrypt' and in_str!='':
        for char in in_str:
            if char != ' ':
                ord_char = (ord(char)-97-key)%26 + 97
                out_str += chr(ord_char)
            else:
                out_str += ''

elif lang == 'rus':
    if mode == 'crypt' and in_str!='':
        for char in in_str:
            if char != ' ':
                out_str += alphabet[(alphabet.find(char) + key) % 33]
            else:
                out_str += ''
    elif mode == 'decrypt' and in_str!='':
        for char in in_str:
            if char != ' ':
                out_str += alphabet[(alphabet.find(char) - key) % 33]
            else:
                out_str += ''
print(out_str)
