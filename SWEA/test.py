indices = set()
k = 3

def gen_idx(i, j, r, c):
    global indices
    if abs(r) + abs(c) == k:
        return

    indices.add((i + r, j + c))
    indices.add((i - r, j - c))
    indices.add((i + r, j - c))
    indices.add((i - r, j + c))
    gen_idx(i, j, r + 1, c)
    gen_idx(i, j, r, c + 1)

gen_idx(0, 0, 0, 0)
print(list(indices))