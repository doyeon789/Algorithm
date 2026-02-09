import sys
sys.setrecursionlimit(10**7)

V = int(input())
edges = list(map(int, input().split()))

tree = [[] for _ in range(V + 1)]
for i in range(0, len(edges), 2):
    parent = edges[i]
    child = edges[i + 1]
    tree[parent].append(child)

preorder = []
inorder = []
postorder = []

def dfs(node):
    if node == 0:
        print(node)
        return

    # 전위 순회
    preorder.append(node)

    # 왼쪽 자식
    if len(tree[node]) >= 1:
        dfs(tree[node][0])

    # 중위 순회
    inorder.append(node)

    # 오른쪽 자식
    if len(tree[node]) == 2:
        dfs(tree[node][1])

    # 후위 순회
    postorder.append(node)

# 루트는 1번
dfs(1)

print(*preorder)
print(*inorder)
print(*postorder)
