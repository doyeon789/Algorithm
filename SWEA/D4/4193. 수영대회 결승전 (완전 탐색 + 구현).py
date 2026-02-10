from collections import deque

def bfs(s_i, s_j):
    q = deque()
    t = 0
    q.append((s_i, s_j, t))

    visited = [[-1]*N for _ in range(N)]
    visited[s_j][s_i] = 0

    while q:
        i, j, t = q.popleft()

        if i == end_i and j == end_j:
            return t

        for d in range(4):
            ni = i + dx[d]
            nj = j + dy[d]
            nt = t + 1

            if not (0 <= ni < N and 0 <= nj < N):
                continue
            if sea[nj][ni] == 1:
                continue

            if sea[nj][ni] == 2:
                if t % 3 != 2:
                    q.append((i, j, t+1))
                    continue

            if visited[nj][ni] != -1:
                continue
            
            visited[nj][ni] = nt
            q.append((ni, nj, nt))

    return -1


dx = [0,1,0,-1]#i
dy = [1,0,-1,0]#j

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    sea = [list(map(int, input().split())) for _ in range(N)]
    start_j, start_i = map(int, input().split())
    end_j, end_i = map(int, input().split())

    result = bfs(start_i,start_j)

    print(f"#{tc} {result}")

""" 제출용 C 마이그레이션

#include <stdio.h>

#define MAXN 10000   // 문제 조건에 맞게 조절
#define QUEUE_SIZE 1000000

typedef struct {
    int i, j, t;
} Node;

Node queue[QUEUE_SIZE];
int front, rear;

int N;
int sea[100][100];
int visited[100][100];

int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

int start_i, start_j, end_i, end_j;

void push(int i, int j, int t) {
    queue[rear++] = (Node){i, j, t};
}

Node pop() {
    return queue[front++];
}

int is_empty() {
    return front == rear;
}

int bfs(int s_i, int s_j) {
    front = rear = 0;

    push(s_i, s_j, 0);
    visited[s_j][s_i] = 0;

    while (!is_empty()) {
        Node cur = pop();
        int i = cur.i;
        int j = cur.j;
        int t = cur.t;

        if (i == end_i && j == end_j) {
            return t;
        }

        for (int d = 0; d < 4; d++) {
            int ni = i + dx[d];
            int nj = j + dy[d];
            int nt = t + 1;

            if (ni < 0 || ni >= N || nj < 0 || nj >= N)
                continue;

            if (sea[nj][ni] == 1)
                continue;

            // 소용돌이
            if (sea[nj][ni] == 2) {
                if (t % 3 != 2) {
                    push(i, j, nt);  // 기다리기
                    continue;
                }
            }

            if (visited[nj][ni] != -1)
                continue;

            visited[nj][ni] = nt;
            push(ni, nj, nt);
        }
    }

    return -1;
}

int main() {
    int T;
    scanf("%d", &T);

    for (int tc = 1; tc <= T; tc++) {
        scanf("%d", &N);

        for (int j = 0; j < N; j++) {
            for (int i = 0; i < N; i++) {
                scanf("%d", &sea[j][i]);
                visited[j][i] = -1;
            }
        }

        scanf("%d %d", &start_j, &start_i);
        scanf("%d %d", &end_j, &end_i);

        int result = bfs(start_i, start_j);
        printf("#%d %d\n", tc, result);
    }

    return 0;
}


"""