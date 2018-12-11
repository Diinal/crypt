import random as rm
from itertools import count


def mutually_prime_number_list(first_num, list_num):
    result = []
    for num in list_num:
        a = first_num
        b = num
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a
        if a+b == 1:
            result.append(num)
    return result


def secret_key(e, f_eiler):
    for d in count(1):
        if (d*e) % f_eiler == 1:
            return d


if __name__ == '__main__':
    crypt_text = []
    decrypt_text = ''
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    p, q, input_text = int(input('write primal p >> ')), int(input('write primal q >> ')), \
                       input('write text for encryption or decryption >> ')

    n = p * q
    f_eiler = (p - 1) * (q - 1)
    e = rm.choice(mutually_prime_number_list(f_eiler, [i for i in range(1, n)]))
    d = secret_key(e, f_eiler)
    print((f_eiler))
    print(e)
    print(d)
    for sym in input_text:
        crypt_text.append((alphabet.find(sym)**e) % n)
    for sym in crypt_text:
        decrypt_text += alphabet[(sym**d) % n]

    print('Encrypted text: %s' % str(crypt_text))
    print('Decrypted text: %s' % decrypt_text)
