import sys 
input = sys.stdin.readline

def bf():
    D = [0] * (N+1)
    
    for i in range(N):
        for start, goal, time in route:
            if D[goal] > D[start] + time:
                D[goal] = D[start] + time
                if i == N-1:
                    return "YES"
    return "NO"

T = int(input())
for _ in range(T):
    N, M ,W = map(int, input().split())
    
    route = []
    for _ in range(M):
        a, b, t = map(int, input().split())
        route.append([a, b, t])
        route.append([b, a, t])
    
    for _ in range(W):
        s, e, t = map(int, input().split())
        route.append([s,e,-t])

    print(bf())