n = int(input())
customers = list(map(int, input().split()))
m, s = map(int, input().split())

answer = 0
for i in range(n):
    rest = customers[i] - m
    answer += 1
    if rest > 0:
        answer += rest // s
        if rest % s > 0 :
            answer += 1

print(answer)