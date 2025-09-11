n, atom_num, k = map(int, input().split())
# x, y, m, s, d
atoms = [list(map(int, input().split())) for _ in range(atom_num)]
grid = []

dirs = {
    0 : [-1, 0],
    1 : [-1, 1],
    2 : [0, 1],
    3 : [1, 1],
    4 : [1, 0],
    5 : [1, -1],
    6 : [0, -1],
    7 : [-1, -1]
}

def move():
    for atom in atoms:
        x, y = atom[0], atom[1]
        m, s, d = atom[2], atom[3] % n, atom[4]
        c_dir = dirs.get(d)

        nx, ny = x + c_dir[0] * s, y + c_dir[1] * s
        if nx > n or nx <= 0:
            if nx > n:
                nx = nx % n
            else:
                nx = n + nx
        if ny > n or ny <= 0:
            if ny > n:
                ny = ny % n
            else:
                ny = n + ny

        atom[0], atom[1] = nx, ny

    return

def check_synthesis():
    global atoms
    total_count = 0
    for a in range(len(atoms) - 1):
        if is_dead(a):
            continue
        cur_m, cur_s = atoms[a][2], atoms[a][3]
        cur_x, cur_y = atoms[a][0], atoms[a][1]
        if atoms[a][4] % 2 == 0:
            have_diagonal, have_orthogonal = False, True
        else:
            have_diagonal, have_orthogonal = True, False

        cur_count = 1
        for b in range(a + 1, len(atoms)):
            if is_dead(b):
                continue
            if cur_x == atoms[b][0] and cur_y == atoms[b][1]:
                cur_count += 1
                cur_m += atoms[b][2]
                cur_s += atoms[b][3]
                if atoms[b][4] % 2 == 0:
                    have_orthogonal = True
                else:
                    have_diagonal = True
                # 해체 처리
                atoms[b] = [-1, -1, -1, -1, -1]


        if cur_m > atoms[a][2]:
            atoms[a] = [-1, -1, -1, -1, -1]
            cur_m_result = cur_m // 5

            if cur_m_result == 0:
                total_count += cur_count
                continue

            cur_s_result = cur_s // cur_count
            if have_diagonal and have_orthogonal:
                for i in range(4):
                    atoms.append([cur_x, cur_y, cur_m_result, cur_s_result, i * 2 + 1])
            else:
                for i in range(4):
                    atoms.append([cur_x, cur_y, cur_m_result, cur_s_result, i * 2])
        total_count += cur_count

    return total_count

def is_dead(idx):
    if atoms[idx][0] == -1 and atoms[idx][1] == -1:
        return True
    return False


def simulate():
    global atoms
    time = 0
    while time < k:
        # print('start')
        # print(atoms)
        # print('move')
        move()
        # print(atoms)
        # print('after syn')
        cut_idx = check_synthesis()
        # print(atoms)
        atoms = atoms[cut_idx:]
        time += 1
    return

def get_total():
    total = 0
    for atom in atoms:
        total += atom[2]
    return total

simulate()
print(get_total())