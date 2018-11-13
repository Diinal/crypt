text = input('write message: ')
size = int(input('write size of matrix 2 or 3: '))
key = []
crypt_text = ''
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

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
def_key = 0

if size == 2:
    def_key = key[0] * key[3] - key[1] * key[2]
elif size == 3:
    def_key = key[0] * key[4] * key[8] + key[1] * key[5] * key[6] + key[3] * key[7] * key[2]
    def_key = def_key - (key[2] * key[4] * key[6] + key[1] * key[3] * key[8] + key[5] * key[7] * key[0])



print(crypt_text)


