
text = "лошмановданиилсергеевич"
abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text1 = []
for i in text:
    text1.append(abc.find(i)+1)
print(text1)
p = 41
g = 6
x = 11
k = 9
y = (g**x) % p

a = (g**k) % p

ax_1 = (a**(p-1-x)) % p

result = []
for i in text1:
    b = ((y**k)*i) % p
    result.append(b)
print(result)
T = []
for i in result:
    T.append((ax_1*i) % p)
print(T)
