in_str = input('Введите входную строку: ')
out_str = ''
print('Введите ключ для шифра Цезаря:')
print('gfzdhhx')
key = int(input('blabal'))
mode = input('Выберите режим(зашифровать - crypt, дешифровать - decrypt): ')

in_str = in_str.lower()
mode = mode.lower()

if mode == 'crypt' and in_str!='':
    for char in in_str:
        ord_char = (ord(char)-97+key)%26 + 97
        out_char = chr(ord_char)
        out_str += out_char
elif mode == 'decrypt' and in_str!='':
    for char in in_str:
        ord_char = (ord(char)-97-key)%26 + 97
        out_char = chr(ord_char)
        out_str += out_char

print(out_str)
