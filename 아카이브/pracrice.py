def findMedianSortedArrays(A, B):
    # 항상 A가 더 짧은 배열이 되도록 (시간복잡도를 log(min(n, m))으로 보장)
    if len(A) > len(B):
        A, B = B, A

    n, m = len(A), len(B)                 # n = len(A), m = len(B)
    total = n + m                         # 총 길이
    half = (total + 1) // 2               # 중앙 기준점 (홀수든 짝수든 왼쪽 파티션 수)

    left, right = 0, n                    # A에서 이진 탐색을 위한 포인터 설정
    while left <= right:
        i = (left + right) // 2           # A에서의 분할 인덱스
        j = half - i                      # B에서의 분할 인덱스 (전체의 절반이 되도록 설정)

        # A와 B에서 분할 후 왼쪽/오른쪽 값 설정 (경계처리 포함)
        A_left = A[i - 1] if i > 0 else float('-inf')  # A의 왼쪽 최대값
        A_right = A[i] if i < n else float('inf')      # A의 오른쪽 최소값
        B_left = B[j - 1] if j > 0 else float('-inf')  # B의 왼쪽 최대값
        B_right = B[j] if j < m else float('inf')      # B의 오른쪽 최소값

        # 올바른 분할 조건: 왼쪽 최대 ≤ 오른쪽 최소
        if A_left <= B_right and B_left <= A_right:
            # 총 개수가 홀수일 경우 → 왼쪽 최대가 중앙값
            if total % 2 == 1:
                return max(A_left, B_left)
            # 총 개수가 짝수일 경우 → 중앙 두 값의 평균
            else:
                return (max(A_left, B_left) + min(A_right, B_right)) / 2

        # A_left가 B_right보다 크면 i를 줄여야 함 (오른쪽이 너무 작음)
        elif A_left > B_right:
            right = i - 1
        # B_left가 A_right보다 크면 i를 늘려야 함 (왼쪽이 너무 작음)
        else:
            left = i + 1
