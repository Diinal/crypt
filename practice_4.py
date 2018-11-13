text = input('Введите исходный текст: ').lower()
gamma = input('Введите гамму: ').lower()

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

dif = round(len(text)/len(gamma)) + 1

gamma *= dif
gamma = gamma[0: len(text)]

crypto_text = ''

choice = 0
while choice != 3:
    crypto_text = ''
    choice = int(input('0 - mod(n) 1-mod(2) 2-ADFGVX 3-exit: '))
    if choice == 0:
        for s in text:
            if s != ' ':
                crypto_text += alphabet[(alphabet.find(s) + alphabet.find(gamma[text.find(s)])) % len(alphabet)]
            else:
                crypto_text += ' '

    if choice == 1:
        for s in text:
            if s != ' ':
                crypto_text += alphabet[(alphabet.find(s) ^ alphabet.find(gamma[text.find(s)])) % len(alphabet)]
            else:
                crypto_text += ' '
    if choice == 2:
        table = dict()
        pre_crypt = ''
        adfgvx = 'ADFGVX'
        format_ = []

        alph = input('Введите перетасованный алфавит для формирования таблицы, '
                     'либо пропустите(будет использован алфавит по умолчанию')
        if alph != '':
            alphabet = alph

        for i in range(len(adfgvx)):
            for j in range(len(adfgvx)):
                    if (6*i + j) < 33:
                        table.update({alphabet[6*i + j]: adfgvx[i] + adfgvx[j]})

        for s in text:
            if s != ' ':
                pre_crypt += table[s]
        len_plus = (len(pre_crypt)//6 + 1) * 6
        pre_crypt += ' ' * (len_plus - len(pre_crypt))

        print(pre_crypt)

        s_gamma = sorted(gamma)
        for i in range(len(gamma)):
            format_.append((s_gamma[i].find(gamma, i) - i) % 6)

        for j in range(6):
            for i in range(len(pre_crypt)//6 + 1):
                if (i*6 + format_[j]) < len(pre_crypt) and pre_crypt[i*6 + format_[j]] != ' ':
                        crypto_text += pre_crypt[i*6 + format_[j]]

    print(crypto_text)
