import sys

text = input('write message: ')
size = int(input('write size of matrix 2 or 3: '))
key = []
crypt_text = ''
decrypt_text = ''
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def determinant():
    if size == 2:
        det_key = key[0] * key[3] - key[1] * key[2]
    elif size == 3:
        det_key = key[0] * key[4] * key[8] + key[1] * key[5] * key[6] + key[3] * key[7] * key[2]
        det_key = det_key - (key[2] * key[4] * key[6] + key[1] * key[3] * key[8] + key[5] * key[7] * key[0])
    return det_key


def obr_element(a, b):
    i = 0
    c = 0
    while c != 1:
        i += 1
        c = a * i % b

    return i


def nod(a, b):
    if a < 0:
        a = a % b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    result = a + b
    if result != 1:
        print("НОД(определитель матрицы,мощности алфавита) не равен 1,дальнейшие действия невозможны")
        sys.exit()


print('write key matrix: ')
for i in range(size ** 2):
    key.append(int(input()))

if len(text) % size != 0:
    text += 'я' * (size - len(text) % size)

if size == 3:
    for i in range(int(len(text) / size)):
        for j in range(size):
            '''print('{0} * {1} + {2} * {3} + {4} * {5} % 33'.format(alphabet.find(text[i]), key[size * j],
                                                                  alphabet.find(text[i+1]), key[size * j + 1],
                                                                  alphabet.find(text[i+2]), key[size * j + 2]))'''

            crypt_text += alphabet[((alphabet.find(text[size*i]) * key[size*j]) +
                                    (alphabet.find(text[size*i + 1]) * key[size*j+1]) +
                                    (alphabet.find(text[size*i + 2]) * key[size*j+2])) % len(alphabet)]

elif size == 2:
    for i in range(len(text) / size):
        for j in range(size):
            crypt_text += alphabet[((alphabet.find(text[size*i]) * key[size * j]) +
                                    (alphabet.find(text[size*i + 1]) * key[size * j + 1])) % len(alphabet)]
#decrypt

det = determinant()

nod(det, len(alphabet))

matrix = []
for i in range(len(key)):
    matrix = key[(i + size) % (size*size-1)]

decrypt_key = key
obr_elem = obr_element(size, len(alphabet))
if size ==2:
    for i in range(len(key)):
        decrypt_key[i] = (matrix[i] * (-1)**i * obr_elem) % len(alphabet)

if size == 3:
    decrypt_key[0] = (matrix[4] * matrix[8] - matrix[5] * matrix[7]) * obr_elem % len(alphabet)
    decrypt_key[1] = -1 * (matrix[3] * matrix[8] - matrix[5] * matrix[6]) * obr_elem % len(alphabet)
    decrypt_key[2] = (matrix[3] * matrix[7] - matrix[4] * matrix[6]) * obr_elem % len(alphabet)
    decrypt_key[3] = -1 * (matrix[1] * matrix[8] - matrix[2] * matrix[7]) * obr_elem % len(alphabet)
    decrypt_key[4] = (matrix[0] * matrix[8] - matrix[2] * matrix[6]) * obr_elem % len(alphabet)
    decrypt_key[5] = -1 * (matrix[0] * matrix[7] - matrix[1] * matrix[6]) * obr_elem % len(alphabet)
    decrypt_key[6] = (matrix[1] * matrix[5] - matrix[4] * matrix[2]) * obr_elem % len(alphabet)
    decrypt_key[7] = -1 * (matrix[0] * matrix[5] - matrix[3] * matrix[2]) * obr_elem % len(alphabet)
    decrypt_key[8] = (matrix[0] * matrix[4] - matrix[3] * matrix[1]) * obr_elem % len(alphabet)

if size == 3:
    for i in range(int(len(crypt_text) / size)):
        for j in range(size):
            '''print('{0} * {1} + {2} * {3} + {4} * {5} % 33'.format(alphabet.find(text[i]), key[size * j],
                                                                  alphabet.find(text[i+1]), key[size * j + 1],
                                                                  alphabet.find(text[i+2]), key[size * j + 2]))'''

            decrypt_text += alphabet[((alphabet.find(crypt_text[size*i]) * decrypt_key[size*j]) +
                                    (alphabet.find(crypt_text[size*i + 1]) * decrypt_key[size*j+1]) +
                                    (alphabet.find(crypt_text[size*i + 2]) * decrypt_key[size*j+2])) % len(alphabet)]

elif size == 2:
    for i in range(len(crypt_text) / size):
        for j in range(size):
            decrypt_text += alphabet[((alphabet.find(crypt_text[size*i]) * decrypt_key[size * j]) +
                                    (alphabet.find(crypt_text[size*i + 1]) * decrypt_key[size * j + 1])) % len(alphabet)]

print(crypt_text)
print(decrypt_text)


