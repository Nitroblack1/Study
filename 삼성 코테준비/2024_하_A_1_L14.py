from collections import deque
import sys

# 입력
n, m, f = map(int, sys.stdin.readline().split())
space = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
e_wall = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
w_wall = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
s_wall = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
n_wall = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
u_wall = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
strange = [tuple(map(int, sys.stdin.readline().split())) for _ in range(f)]

# 면 상수
EAST, WEST, SOUTH, NORTH, TOP = 0, 1, 2, 3, 4
views = [e_wall, w_wall, s_wall, n_wall, u_wall]

# ---------------- Phase 1: 시간의 벽 표면 탈출 ---------------- #
def find_exit_and_goal(wall_base_r, wall_base_c):
    """ 출구 좌표와 벽 단면 내 목표 좌표 계산 """
    plane_exit_r, plane_exit_c = -1, -1
    goal_face, goal_r, goal_c = -1, -1, -1

    # 북쪽
    if wall_base_r > 0:
        for c_off in range(m):
            if space[wall_base_r-1][wall_base_c+c_off] == 0:
                plane_exit_r, plane_exit_c = wall_base_r-1, wall_base_c+c_off
                goal_face, goal_r, goal_c = NORTH, m-1, m-c_off-1
                return plane_exit_r, plane_exit_c, goal_face, goal_r, goal_c

    # 남쪽
    if wall_base_r+m < n:
        for c_off in range(m):
            if space[wall_base_r+m][wall_base_c+c_off] == 0:
                plane_exit_r, plane_exit_c = wall_base_r+m, wall_base_c+c_off
                goal_face, goal_r, goal_c = SOUTH, m-1, c_off
                return plane_exit_r, plane_exit_c, goal_face, goal_r, goal_c

    # 서쪽
    if wall_base_c > 0:
        for r_off in range(m):
            if space[wall_base_r+r_off][wall_base_c-1] == 0:
                plane_exit_r, plane_exit_c = wall_base_r+r_off, wall_base_c-1
                goal_face, goal_r, goal_c = WEST, m-1, r_off
                return plane_exit_r, plane_exit_c, goal_face, goal_r, goal_c

    # 동쪽
    if wall_base_c+m < n:
        for r_off in range(m):
            if space[wall_base_r+r_off][wall_base_c+m] == 0:
                plane_exit_r, plane_exit_c = wall_base_r+r_off, wall_base_c+m
                goal_face, goal_r, goal_c = EAST, m-1, m-r_off-1
                return plane_exit_r, plane_exit_c, goal_face, goal_r, goal_c

    return plane_exit_r, plane_exit_c, goal_face, goal_r, goal_c


def calc_escape_time_3d():
    """ 표면 BFS로 시간의 벽 탈출 시간 계산 """
    # 시작점 찾기
    start_face, sr, sc = -1, -1, -1
    for r in range(m):
        for c in range(m):
            if u_wall[r][c] == 2:
                start_face, sr, sc = TOP, r, c
                u_wall[r][c] = 0
                break
        if start_face != -1: break

    # 시간의 벽 좌표 찾기
    wall_base_r, wall_base_c = -1, -1
    for r in range(n):
        if 3 in space[r]:
            wall_base_r, wall_base_c = r, space[r].index(3)
            break

    # 출구 매핑
    plane_exit_r, plane_exit_c, goal_face, goal_r, goal_c = find_exit_and_goal(wall_base_r, wall_base_c)
    if goal_face == -1 or views[goal_face][goal_r][goal_c] == 1:
        return -1, -1, -1

    q = deque([(0, start_face, sr, sc)])
    visited = [[[False]*m for _ in range(m)] for _ in range(5)]
    visited[start_face][sr][sc] = True

    while q:
        t, face, r, c = q.popleft()
        if (face, r, c) == (goal_face, goal_r, goal_c):
            return t+1, plane_exit_r, plane_exit_c

        # 같은 면 이동
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<m and 0<=nc<m and views[face][nr][nc]==0 and not visited[face][nr][nc]:
                visited[face][nr][nc]=True
                q.append((t+1, face, nr, nc))

        # 면 전환 (명시적 규칙)
        transitions=[]
        if face==TOP:
            if r==0: transitions.append((NORTH,0,m-c-1))
            if r==m-1: transitions.append((SOUTH,0,c))
            if c==0: transitions.append((WEST,0,r))
            if c==m-1: transitions.append((EAST,0,m-r-1))
        elif face==NORTH:
            if r==0: transitions.append((TOP,0,m-c-1))
            if c==m-1: transitions.append((WEST,r,0))
            if c==0: transitions.append((EAST,r,m-1))
        elif face==SOUTH:
            if r==0: transitions.append((TOP,m-1,c))
            if c==0: transitions.append((WEST,r,m-1))
            if c==m-1: transitions.append((EAST,r,0))
        elif face==WEST:
            if r==0: transitions.append((TOP,c,0))
            if c==0: transitions.append((NORTH,r,m-1))
            if c==m-1: transitions.append((SOUTH,r,0))
        elif face==EAST:
            if r==0: transitions.append((TOP,m-c-1,m-1))
            if c==m-1: transitions.append((NORTH,r,0))
            if c==0: transitions.append((SOUTH,r,m-1))

        for nf,nr,nc in transitions:
            if views[nf][nr][nc]==0 and not visited[nf][nr][nc]:
                visited[nf][nr][nc]=True
                q.append((t+1,nf,nr,nc))

    return -1,-1,-1

# ---------------- Phase 2: 평면 BFS (이상 현상) ---------------- #
def calc_dest_time_2d(time_to_exit_wall, sr, sc):
    if time_to_exit_wall==-1: return -1

    # 탈출구 찾기
    er,ec=-1,-1
    for r in range(n):
        if 4 in space[r]:
            er,ec=r,space[r].index(4)
            break

    anomaly_blocks=[[float('inf')]*n for _ in range(n)]
    adr,adc=[0,0,1,-1],[1,-1,0,0] # 동서남북

    for r0,c0,d,v in strange:
        if space[r0][c0]!=4:
            anomaly_blocks[r0][c0]=min(anomaly_blocks[r0][c0],0)
        t=v; r,c=r0,c0
        while True:
            r+=adr[d]; c+=adc[d]
            if not(0<=r<n and 0<=c<n) or space[r][c] in [1,4]: break
            anomaly_blocks[r][c]=min(anomaly_blocks[r][c],t)
            t+=v

    q=deque([(time_to_exit_wall,sr,sc)])
    visited=[[float('inf')]*n for _ in range(n)]
    visited[sr][sc]=time_to_exit_wall

    while q:
        t,r,c=q.popleft()
        if (r,c)==(er,ec): return t
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr,nc=r+dr,c+dc; nt=t+1
            if 0<=nr<n and 0<=nc<n and space[nr][nc] not in [1,3] \
               and nt<anomaly_blocks[nr][nc] and nt<visited[nr][nc]:
                visited[nr][nc]=nt
                q.append((nt,nr,nc))
    return -1

# ---------------- 실행 ---------------- #
time_to_exit_wall,sr,sc=calc_escape_time_3d()
ans=calc_dest_time_2d(time_to_exit_wall,sr,sc)
print(ans)
