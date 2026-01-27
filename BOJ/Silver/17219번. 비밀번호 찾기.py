import sys

n, m = map(int, sys.stdin.readline().split())
site = dict()

for _ in range(n):
    id, pw = map(str, sys.stdin.readline().split())
    site[id] = pw

for _ in range(m):
    address = str(sys.stdin.readline().rstrip())
    print(site[address])
