s = input()
alphabet = {}

for ch in s:
    alphabet[ch] = alphabet.get(ch, 0) + 1

odd = 0
center = ""

for k in alphabet:
    if alphabet[k] % 2 == 1:
        odd += 1
        center = k

if odd > 1:
    print("I'm Sorry Hansoo")
else:
    left = []

    for k in sorted(alphabet.keys()):
        left.append(k * (alphabet[k] // 2))

    left = ''.join(left)
    print(left + center + left[::-1])
