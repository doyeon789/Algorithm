import sys
input = sys.stdin.readline
from math import gcd

MOD = 1000000007

M = int(input())
ans = 0
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a // gcd(a, b), b // gcd(a, b)
    ans += (b * pow(a, -1, MOD)) % MOD
    ans %= MOD
print(ans)