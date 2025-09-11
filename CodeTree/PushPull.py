# n, t = map(int, input().split())
# u = list(map(int, input().split()))
# d = list(map(int, input().split()))
#
# # Please write your code here.
#
# for _ in range(t):
#     u_temp = u[n-1]
#     d_temp = d[n-1]
#
#     for j in range(n-1, 0, -1):
#         u[j] = u[j-1]
#         d[j] = d[j-1]
#     u[0] = d_temp
#     d[0] = u_temp
#
# for element in u:
#     print(element, end=" ")
#
# print()
#
# for element in d:
#     print(element, end=" ")

n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
for _ in range(t):
    l_temp = l[n-1]
    r_temp = r[n-1]
    d_temp = d[n-1]

    for i in range(n-1, 0, -1):
        l[i] = l[i-1]
        r[i] = r[i-1]
        d[i] = d[i-1]

    l[0] = d_temp
    r[0] = l_temp
    d[0] = r_temp

for element in l:
    print(element, end=" ")
print()
for element in r:
    print(element, end=" ")
print()
for element in d:
    print(element, end=" ")