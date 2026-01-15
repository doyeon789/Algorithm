s = input()     # 입력
alphabet = {}   # 알파벳과 그 수를 저장할 딕셔너리

# 딕셔너리에 알파벳과 그 수를 저장
for ch in s: 
    alphabet[ch] = alphabet.get(ch, 0) + 1

# odd : 홀수 갯수를 저장, center : 출력할때 중간 값 저장
odd = 0
center = ""

for k in alphabet:
    # 알파벳의 갯수가 홀수 일때
    if alphabet[k] % 2 == 1:
        odd += 1 # odd에 저장
        center = k # 홀수 일때의 알파벳을 저장

# 홀수의 갯수가 1초과일때는 X
if odd > 1:
    print("I'm Sorry Hansoo")
else:
    # 정답의 왼쪽을 저장할 리스트
    left = []
    
    # 알파벳의 오름차순으로 정렬하여 각각의 키를 k에 넣어주기
    for k in sorted(alphabet.keys()):
        # left에 알파벳을 그 갯수의 반만큼을 추가
        left.append(k * (alphabet[k] // 2))
    #left를 하나의 문자열로 바꾸기
    left = ''.join(left)
    #left와 center(중간값)와 left의 역순을 출력
    print(left + center + left[::-1])
