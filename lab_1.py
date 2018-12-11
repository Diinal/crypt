import random

text = input('text >>')
len_key = int(input('length of key >>'))

if len(text) % len_key != 0:
    text += ' ' * (len_key - (len(text) % len_key))


enc_key = [i for i in range (1, len_key+1)]
enc_key = sorted(enc_key, key=lambda *args: random.random())
print('key =', enc_key)

enc_text_arr = [['a']*len_key for j in range(int(round(len(text)/len_key)))]

c = 0
for i in range(len_key):
    for j in range(int(round(len(text)/len_key))):
        enc_text_arr[j][i] = text[c]
        c += 1
print(enc_text_arr)

enc_text = ''
for i in range(int(round(len(text)/len_key))):
    for j in enc_key:
        enc_text += enc_text_arr[i][j-1]
print('=' * 30)
print('encrypted text:', enc_text)

dec_text_arr = [['a']*len_key for j in range(int(round(len(text)/len_key)))]

c = 0
for i in range(int(round(len(enc_text)/len_key))):
    for j in range(len_key):
        dec_text_arr[i][j] = enc_text[c]
        c += 1
print(dec_text_arr)

dec_text = ''
for j in enc_key:
    for i in range(int(round(len(enc_text)/len_key))):
        dec_text += dec_text_arr[i][j-1]
print('=' * 30)
print('decrypted text:', dec_text)
