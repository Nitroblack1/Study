w1 = [3,5]
w2 = [1,4]
w3 = [0,4]
w4 = [1,3]

m = (4, 1)

ws = [w1, w2, w3, w4]

ws.sort(key=lambda x: (abs(x[0] -  m[0]), abs(x[1] - m[1])))
print(ws)