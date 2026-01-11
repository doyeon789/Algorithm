alphabet = input().strip()

a_num = [ord(al) - ord('A') + 1 for al in alphabet]

print(*a_num)
