from collections import deque


class Queue:
    def __init__(self):
        self.dq = deque()

    def push(self, item):
        self.dq.append(item)

    def empty(self):
        return not self.dq

    def size(self):
        return len(self.dq)

    def pop(self):
        if self.empty():
            raise Exception("Queue is empty")
        return self.dq.popleft()

    def front(self):
        if self.empty():
            raise Exception("Queue is empty")
        return self.dq[0]


#### Main Function ####

n, k = map(int, input().split())
people = Queue()

for i in range(1, n + 1):
    people.push(i)

while people.size() != 0:
    turn = 0
    while turn < k - 1:
        people.push(people.pop())
        turn += 1

    print(people.pop(), end=" ")