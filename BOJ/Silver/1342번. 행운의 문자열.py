from collections import Counter
import sys

def backTracking(prev, length):
    global ans
    if length == len(string):
        ans += 1
        return
    
    for ch in cnt:
        if cnt[ch] > 0 and ch != prev:
            cnt[ch] -= 1
            backTracking(ch, length + 1)
            cnt[ch] += 1

string = string = sys.stdin.readline().strip()
cnt = Counter(string)
ans = 0 
backTracking('', 0)
print(ans)
