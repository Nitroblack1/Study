n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Please write your code here.

# 1 2 3 1 1 5
# blocks[s1-1] ~ blocks[e1-1] delete
# temp 배열을 만들어서 [2,4] 인덱스는 건너뛰고 추가하면 되잖아?
# 그리고 원래 blocks에 넣으면 되는거지.

temp = []
for i in range(len(blocks)):
    if s1-1 <= i <= e1-1:
        continue
    else:
        temp.append(blocks[i])

blocks = list.copy(temp)

temp = []
for i in range(len(blocks)):
    if s2-1 <= i <= e2-1:
        continue
    else:
        temp.append(blocks[i])

blocks = list.copy(temp)

print(len(blocks))
for element in blocks:
    print(element)