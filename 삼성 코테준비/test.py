from collections import deque

def rotate_matrix(arr, R):
    N = len(arr)
    M = len(arr[0])
    layers = min(N, M) // 2  # 레이어 개수

    for layer in range(layers):
        q = deque()

        # 1. 레이어 껍질 꺼내기
        # 위쪽 행
        for y in range(layer, M - layer):
            q.append(arr[layer][y])
        # 오른쪽 열
        for x in range(layer + 1, N - layer - 1):
            q.append(arr[x][M - layer - 1])
        # 아래쪽 행
        for y in range(M - layer - 1, layer - 1, -1):
            q.append(arr[N - layer - 1][y])
        # 왼쪽 열
        for x in range(N - layer - 2, layer, -1):
            q.append(arr[x][layer])

        # 2. 회전 (R만큼 왼쪽으로)
        q.rotate(-(R % len(q)))

        # 3. 다시 채워넣기
        # 위쪽 행
        for y in range(layer, M - layer):
            arr[layer][y] = q.popleft()
        # 오른쪽 열
        for x in range(layer + 1, N - layer - 1):
            arr[x][M - layer - 1] = q.popleft()
        # 아래쪽 행
        for y in range(M - layer - 1, layer - 1, -1):
            arr[N - layer - 1][y] = q.popleft()
        # 왼쪽 열
        for x in range(N - layer - 2, layer, -1):
            arr[x][layer] = q.popleft()
    return arr


def debug(matrix):
    for r in matrix:
        for c in r:
            print(c, end=" ")
        print()

array = [list(map(int, input().split())) for _ in range(4)]
debug(rotate_matrix(array, 2))