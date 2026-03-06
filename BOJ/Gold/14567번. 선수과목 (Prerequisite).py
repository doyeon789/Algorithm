from collections import deque

n, m = map(int, input().split())

# 그래프와 진입차수 배열
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)

# 선수과목 관계 입력
# a -> b : a를 먼저 들어야 b를 들을 수 있음
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1 # 진입차수 개수 + 1


# 각 과목을 들을 수 있는 최소 학기
result = [0]*(n+1)

q = deque()
for i in range(1, n+1):
    # 진입차수가 0인것 q에 넣어두기
    if indegree[i] == 0:
        q.append(i)
        result[i] = 1 # 학기 1로 초기화

# 위상정렬 시작
while q:
    now = q.popleft() # 현재 과목

    # 현재 과목을 선수로 가지는 다음 과목들 확인
    for g in graph[now]:
        # 선수과목 하나 처리했으므로 진입차수 감소
        indegree[g] -= 1

        # g 과목은 now 과목 다음 학기부터 가능
        # 여러 선수과목이 있을 수 있으므로 최대값 갱신
        result[g] = max(result[g], result[now] + 1)

        # 모든 선수과목이 처리되면 큐에 추가
        if indegree[g] == 0:
            q.append(g)
            

# 1번 과목부터 출력
print(*result[1:])