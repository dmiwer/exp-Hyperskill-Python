def matrix_by_matrix(m1, m2):
    mr = [[0] * len(m2[0]) for _ in range(len(m1))]
    for i in range(len(mr)):
        for j in range(len(mr[0])):
            mr[i][j] = sum([m1[i][x] * m2[x][j] for x in range(len(m2))])
    return mr


def matrix_by_const(m1, c):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j] *= c
    return m1


def sum_mat(m1, m2):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j] += m2[i][j]
    return m1


def show_matrix(res_matrix):
    print("The result is:")
    for x in range(len(res_matrix)):
        print(*[res_matrix[x][y] for y in range(len(res_matrix[0]))])


def get_matrix(title, x, y):
    print(title)
    return [[float(el) for el in input().split(" ")] for _ in range(x)]


def show_err():
    print("The operation cannot be performed.")


def get_choice():
    return int(input("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit
Your choice: """))


def add_matrices():
    ax, ay = map(int, input("Enter size of first matrix: ").split(" "))
    m1 = get_matrix("Enter first matrix:", ax, ay)
    bx, by = map(int, input("Enter size of second matrix: ").split(" "))
    if ax != bx or ay != by:
        show_err()
        return
    m2 = get_matrix("Enter second matrix: ", bx, by)
    res_matrix = sum_mat(m1, m2)
    show_matrix(res_matrix)


def mul_by_matrix():
    ax, ay = map(int, input("Enter size of first matrix: ").split(" "))
    m1 = get_matrix("Enter first matrix: ", ax, ay)
    bx, by = map(int, input("Enter size of second matrix: ").split(" "))
    if ay != bx:
        show_err()
        return
    m2 = get_matrix("Enter second matrix: ", bx, by)
    res_matrix = matrix_by_matrix(m1, m2)
    show_matrix(res_matrix)


def mul_by_const():
    ax, ay = map(int, input("Enter size of matrix: ").split(" "))
    m1 = get_matrix("Enter matrix: ", ax, ay)
    c = float(input("Enter constant: "))
    res_matrix = matrix_by_const(m1, c)
    show_matrix(res_matrix)


def execute(choice):
    if choice == 1:
        add_matrices()
    elif choice == 2:
        mul_by_const()
    elif choice == 3:
        mul_by_matrix()
    return


while True:
    choice = get_choice()
    if choice == 0:
        break
    execute(choice)
    print()
