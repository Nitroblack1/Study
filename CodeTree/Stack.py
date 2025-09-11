class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        return int(not self.items)

    def size(self):
        return len(self.items)

    def top(self):
        if self.empty():
            return 'stack is empty'
        return self.items[-1]

    def pop(self):
        if self.empty():
            return 'stack is empty'
        return self.items.pop()

    def push(self, item):
        self.items.append(item)


####################################

N = int(input())
command = []
value = []
st = Stack()

for _ in range(N):
    line = input().split()
    if line[0] == 'push':
        st.push(int(line[1]))
    elif line[0] == 'pop':
        print(st.pop())
    elif line[0] == 'top':
        print(st.top())
    elif line[0] == 'size':
        print(st.size())
    elif line[0] == 'empty':
        print(st.empty())