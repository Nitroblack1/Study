n, m, q = map(int, input().split())

# Create 2D array for building state
a = [list(map(int, input().split())) for _ in range(n)]

# Process wind queries
winds = [tuple(map(int, input().split())) for _ in range(q)]

##################################################################
# Please write your code here.
##################################################################

# Rotate boundary
def rotate(r1, c1, r2, c2):
    temp = a[r1][c2]

    # top array shift
    for j in range(c2, c1, -1):
        a[r1][j] = a[r1][j-1]

    # left array shift
    for i in range(r1, r2):
        a[i][c1] = a[i+1][c1]

    # bottom array shift
    for j in range(c1, c2):
        a[r2][j] = a[r2][j+1]

    # right array shift
    for i in range(r2, r1, -1):
        a[i][c2] = a[i-1][c2]

    a[r1+1][c2] = temp  # 데이터 보정


# Averaging inner numbers
dis = [0,0,1,-1]    # 우, 좌, 하, 상
djs = [1,-1,0,0]

def is_inbound(i, j):
    if 0 <= i < n and 0 <= j < m:
        return True
    return False

def averaging(r1, c1, r2, c2):
    temp_board = [x[:] for x in a]
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            current_sum = a[i][j]
            divider = 1
            for di, dj in zip(dis, djs):
                if is_inbound(i+di, j+dj):
                    current_sum += a[i+di][j+dj]
                    divider += 1
            temp_board[i][j] = current_sum // divider
    return temp_board

##################################################################

for wind in winds:
    rotate(wind[0]-1, wind[1]-1, wind[2]-1, wind[3]-1)
    a = averaging(wind[0]-1, wind[1]-1, wind[2]-1, wind[3]-1)

for row in a:
    for element in row:
        print(element, end=" ")
    print()