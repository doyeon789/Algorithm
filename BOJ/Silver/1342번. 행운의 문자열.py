from collections import Counter

string = input()
N = len(string)

cnt = Counter(string)

ans = 0 
def dfs(prev, length):
    global ans
    if length == N:
        ans += 1
        return
    
    for ch in cnt:
        if cnt[ch] > 0 and ch != prev:
            cnt[ch] -= 1
            dfs(ch, length + 1)
            cnt[ch] += 1
dfs('', 0)

print(ans)
