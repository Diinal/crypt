in_str = input('Введите входную строку: ').lower()
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
range_symbols = 0

symbols = dict()  # инициализация словаря с уникальными символами
for a in in_str:
    if a not in symbols and a != " ":
        temp = {a: 0}
        symbols.update(temp)
        range_symbols += 1

for a in in_str:
    if a != " ":
        symbols[a] += 1

for i in range(0, range_symbols, 1):
    m = 0
    del_sym = ""
    key = 0
    out_str = ""

    for b in symbols:
        if symbols[b] > m:
            m = symbols[b]
            key = (alphabet.find(b) - alphabet.find('о')) % 33
            del_sym = b

    del symbols[del_sym]

    for char in in_str:
        if char != ' ':
            out_str += alphabet[(alphabet.find(char) - key) % 33]
        else:
            out_str += ' '

    print('Key = ' + str(key) + " " + out_str)

