# [HLD (Heavy Light Decomposition)]
# HLD느 트리를 몇 개의 체인으로 분할하여 임의의 두 정점 사이의 경로에 최대 logN개의 
#   체인만 존재하다로고 하는 자료구조 
# 각각의 체인을 효율적으로 관리할 수 있수 있는 자료구조 : 세그먼트 트리, 펜윅트리 ...

# HLD는 간선을 무거운 간선과 가벼운 간선으로 구분한다.
#   size(son) > size(parent)/2 를 만족하면 무거운 간선, else => 가벼운 간선
#   한 정점에서 밑으로 내려가는 가선중에서 무거운 간선은 최대 한개만 존재해야함.
#   (보통 무거운 간선은 size(son)이 가장 큰 간선으로 기준.)

# modify(a, b) -> a번 노드 값에 b를 더함
# go(a,b) -> a~b 경로에서 최대값 출력


import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# 입력
n = int(input())
g = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

# HLD 관련 배열
size = [0] * n
parent = [0] * n
depth = [0] * n
heavy = [-1] * n

chain = [0] * n
num = [0] * n
top = [0] * n
csz = [0] * n

# 세그트리
tree = [0] * (4 * n)

cur_pos = 0
chain_cnt = 0


# ---------------- DFS (heavy child 찾기) ----------------
def dfs(v, p):
    size[v] = 1
    parent[v] = p
    max_size = 0

    for to in g[v]:
        if to == p:
            continue
        depth[to] = depth[v] + 1
        dfs(to, v)
        size[v] += size[to]

        if size[to] > max_size:
            max_size = size[to]
            heavy[v] = to


# ---------------- HLD 구성 ----------------
def hld(v, head):
    global cur_pos, chain_cnt

    if head == v:
        chain_cnt += 1

    chain[v] = chain_cnt - 1
    top[chain_cnt - 1] = head
    num[v] = cur_pos
    cur_pos += 1
    csz[chain_cnt - 1] += 1

    if heavy[v] != -1:
        hld(heavy[v], head)

    for to in g[v]:
        if to != parent[v] and to != heavy[v]:
            hld(to, to)


# ---------------- 세그트리 ----------------
def update(node, start, end, idx, value):
    if start == end:
        tree[node] += value
        return
    mid = (start + end) // 2
    if idx <= mid:
        update(node * 2, start, mid, idx, value)
    else:
        update(node * 2 + 1, mid + 1, end, idx, value)

    tree[node] = max(tree[node * 2], tree[node * 2 + 1])


def query(node, start, end, l, r):
    if r < start or end < l:
        return 0
    if l <= start and end <= r:
        return tree[node]

    mid = (start + end) // 2
    return max(
        query(node * 2, start, mid, l, r),
        query(node * 2 + 1, mid + 1, end, l, r),
    )


# ---------------- 경로 쿼리 ----------------
def path_query(a, b):
    res = 0
    while chain[a] != chain[b]:
        if depth[top[chain[a]]] < depth[top[chain[b]]]:
            a, b = b, a

        head = top[chain[a]]
        res = max(res, query(1, 0, n - 1, num[head], num[a]))
        a = parent[head]

    if depth[a] > depth[b]:
        a, b = b, a

    res = max(res, query(1, 0, n - 1, num[a], num[b]))
    return res


def modify(a, val):
    update(1, 0, n - 1, num[a], val)


# ---------------- 실행 ----------------
dfs(0, -1)
hld(0, 0)

m = int(input())
for _ in range(m):
    tmp = input().split()
    if tmp[0] == 'G':
        a = int(tmp[1]) - 1
        b = int(tmp[2]) - 1
        print(path_query(a, b))
    else:
        a = int(tmp[1]) - 1
        b = int(tmp[2])
        modify(a, b)