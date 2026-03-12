str1 = input()
str2 = input()

LCS = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]

flag = 1
for i in range(1,len(str1)+1):
    for j in range(1,len(str2)+1):
        if str1[i-1] == str2[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

print(LCS[len(str1)][len(str2)])

i = len(str1)
j = len(str2)

result = []

while i > 0 and j > 0:
    if str1[i-1] == str2[j-1]:
        result.append(str1[i-1])
        i -= 1
        j -= 1
    elif LCS[i-1][j] > LCS[i][j-1]:
        i -= 1
    else:
        j -= 1

result.reverse()
print("".join(result))