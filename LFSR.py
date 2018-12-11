#LFSR = linear feedback shift register
#РСЛОС = регистр сдвига с линейной обратной связью

cp_str = input('input degrees of characteristic polynomial(example: x^4 + x + 1 = 4 1 0 ) >> ')
state_str = input('input the initial state of the shift register(example: 0110) >> ')

cp = []
state = []
key = []

for s in cp_str:
    if s != ' ' and s != '0':
        cp.append(int(s))

for s in state_str:
    state.append(int(s))

next_state = state.copy()

for i in range(2 ** len(state_str)-1):
    state = next_state.copy()
    key.append(state[len(state)-1])
    next_state[0] = next_state[cp[0]-1]

    for a in range(len(cp)-1):
        next_state[0] ^= state[cp[a+1]-1]

    next_state[1:] = state[:-1]
    print(str(state) + 'key:' + str(key[i]))
