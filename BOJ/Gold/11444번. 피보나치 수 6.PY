import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 1000000007

m = {
    0: 0,
    1: 1,
    2: 1
}

def fib(x):
    if x in m:
        return m[x]

    if x % 2 == 0:
        result = fib(x//2) * (fib(x//2 + 1) + fib(x//2 - 1)) % MOD
    else:
        result = (
            (fib((x+1)//2) * fib((x+1)//2)) % MOD +
            (fib((x-1)//2) * fib((x-1)//2)) % MOD
        ) % MOD

    m[x] = result
    return result

n = int(input())
print(fib(n))