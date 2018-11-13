value = input('enter value: ')
percent = input('enter percent %: ')
tick = input('enter tick: ')

tick = int(tick)

while tick != 0:
    value = int(value) * (int(percent)/100) + int(value)
    tick -= 1

print(int(value))
