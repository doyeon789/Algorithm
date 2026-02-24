def dfs(d_count, x,y,dir,now,startX,startY, visited):
    global res
    if d_count > 3: 
        return
    
    if d_count == 3 and (x,y) == (startX,startY):
        res = max(res, now)
    else:
        for i in range(2):
            d = (dir + i) % 4
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if dessert[nx][ny] not in visited:
                    visited.append(dessert[nx][ny])
                    dfs(d_count+i, nx,ny,d, now+1, startX,startY, visited)
                    visited.pop()

dx = [1,1,-1,-1]
dy = [-1,1,1,-1]

T = int(input())
for t in range(1,T+1):
    n = int(input())
    dessert = [list(map(int, input().split())) for _ in range(n)]

    res = -1
    for x in range(n):
        for y in range(n):
            dfs(0,x,y,0,0,x,y, [])

    print(f"#{t} {res}")
