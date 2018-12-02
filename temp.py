a = 72
b = 5

while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a

print(a + b)