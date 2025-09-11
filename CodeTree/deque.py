from collections import deque

dq = deque()

n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == 'push_front':
        dq.appendleft(command[1])
    if command[0] == 'push_back':
        dq.append(command[1])
    if command[0] == 'pop_front':
        print(dq.popleft)
    if command[0] == 'pop_back':
        print(dq.pop())
    if command[0] == 'size':
        print(len(dq))
    if command[0] == 'empty':
        if dq:
            print(1)
        else:
            print(0)
    if command[0] == 'front':
        print(dq[0])
    if command[0] == 'back':
        print(dq[-1])
