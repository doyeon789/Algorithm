import sys   
input = sys.stdin.readline  
from bisect import bisect_right  

def find(x):  
    if x != parents[x]:  
        parents[x] = find(parents[x])  
    return parents[x]  

def union(x, y):  
    if y >= M:  
        return  
    x = find(x)  
    y = find(y)  
    parents[x] = y  

N, M, K = map(int, input().split())  
cards = [*map(int, input().split())]  
chulsoo = [*map(int, input().split())]  
parents = [i for i in range(M)]  
cards.sort()  
for i in chulsoo:  
    idx = bisect_right(cards, i)  
    idx = find(idx)  
    print(cards[idx])  
    union(idx, idx+1)