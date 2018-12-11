from RSA import mutually_prime_number_list as mpnl
import random as rm


def bezout_x(a, arr, m):
    for x in arr:
        if (x*a) % m ==1:
            return x


def backpack_package(num, key):
    result = ''
    key.sort(reverse = True)
    for i, a in enumerate(key):
        if a > num:
            result += '0'
        else:
            num -= a
            result += '1'
    if num == 0:
        return result[::-1]
    else:
        print("Error! backpack can't packaged")

def bin_to_int(arr):
    result = [0 for i in range(len(arr))]
    for i, pack in enumerate(arr):
        pack = pack[::-1]
        number = 0
        for j, bit in enumerate(pack):
            if bit == '1':
                result[i] += 2**j
    return result


#text = input('text >>')
text = 'эльгамальусовершенствовалсистемудиффихеллманаиполучилдваалгоритма'
#key = input('over grow sequence >>')
#key = [key.split()]
e_key = (62, 93, 186, 403, 417, 352, 315, 210)

bin_text = text.encode('windows-1251')
bin_arr = [format(x, 'b') for x in bin_text]
print(bin_arr)

enc_text = [0 for i in range(len(bin_arr))]

for counter, pack in enumerate(bin_arr):
    for i, bite in enumerate(pack):
        if bite == '1':
            enc_text[counter] += e_key[i]

print(text)
print(enc_text)

d_key = [2, 3, 6, 13, 27, 52, 105, 210]

m = rm.randrange(1, 20) + sum(d_key)
m=420
print(sum(d_key))
n = rm.choice(mpnl(m, [i for i in range(1, m)]))
n=31
nn = (bezout_x(n, [i for i in range(2, m)], m))
print(m, n, nn)

dec_bin_text = []
predec_text = []

for sym in enc_text:
    dec_bin_text.append(backpack_package(((sym*nn) % m), d_key))

print(dec_bin_text)
dec_text = ''
dec_bin_text = bin_to_int(dec_bin_text)
print(dec_bin_text)
for a in dec_bin_text:
    dec_text += chr(a + 848)
print(dec_text)
