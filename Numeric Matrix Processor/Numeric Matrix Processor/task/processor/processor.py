class Matrix:
    def __init__(self, height, length):
        self.height = height
        self.length = length
        self.arr = []

    @staticmethod
    def get(arr: list):
        ans = Matrix(len(arr), len(arr[0]))
        ans.arr = arr
        return ans

    def show(self):
        for h in range(self.height):
            print(*[self.arr[h][l] for l in range(self.length)])

    def fill(self):
        temp = []
        for i in range(self.height):
            t = list(map(float, input().split(" ")))
            if len(t) != self.length:
                return -1
            temp.append(t)
        self.arr = temp

    def sum(self, other):
        return Matrix.get([[(self.arr[i][j] + other.arr[i][j]) for j in range(self.length)] for i in range(self.height)])

    def mul(self, other):
        if type(other) == type(2.3):
            return Matrix.get([[(self.arr[i][j] * other) for j in range(self.length)] for i in range(self.height)])
        elif type(other) == type(self):
            return Matrix.get([[sum(self.arr[i][x] * other.arr[x][j] for x in range(self.length)) for j in range(other.length)] for i in range(self.height)])
        else:
            return -1

    def transpose(self, n):
        if n == 1:
            return Matrix.get([[self.arr[j][i] for j in range(self.length)] for i in range(self.height)])
        elif n == 2:
            return Matrix.get([[self.arr[j][i] for j in reversed(range(self.length))] for i in reversed(range(self.height))])
        elif n == 3:
            return Matrix.get([[self.arr[i][j] for j in reversed(range(self.length))] for i in range(self.height)])
        elif n == 4:
            return Matrix.get([[self.arr[i][j] for j in range(self.length)] for i in reversed(range(self.height))])
        else:
            return -1


def add_matrices():
    m1_height, m1_length = map(int, input("Enter size of first matrix: ").split(" "))
    print("Enter first matrix: ")
    m1 = Matrix(m1_height, m1_length)
    m1.fill()
    m2_height, m2_length = map(int, input("Enter size of second matrix: ").split(" "))
    print("Enter second matrix: ")
    if m1_height != m2_height or m1_length != m2_length:
        show_err()
        return
    m2 = Matrix(m2_height, m2_length)
    m2.fill()
    res_matrix = m1.sum(m2)
    print("The result is:")
    res_matrix.show()


def mul_by_matrix():
    m1_height, m1_length = map(int, input("Enter size of first matrix: ").split(" "))
    print("Enter first matrix: ")
    m1 = Matrix(m1_height, m1_length)
    m1.fill()
    m2_height, m2_length = map(int, input("Enter size of second matrix: ").split(" "))
    print("Enter second matrix: ")
    if m1_length != m2_height:
        show_err()
        return
    m2 = Matrix(m2_height, m2_length)
    m2.fill()
    res_matrix = m1.mul(m2)
    print("The result is:")
    res_matrix.show()


def mul_by_const():
    m1_height, m1_length = map(int, input("Enter size of first matrix: ").split(" "))
    print("Enter matrix: ")
    m1 = Matrix(m1_height, m1_length)
    m1.fill()
    c = float(input("Enter constant: "))
    res_matrix = m1.mul(c)
    print("The result is:")
    res_matrix.show()


def transpose_matrix():
    n = int(input("""
1. Main diagonal
2. Said diagonal
3. Vertical line
4. Horizontal line
Your choice: """))
    m1_height, m1_length = map(int, input("Enter matrix size: ").split(" "))
    print("Enter matrix: ")
    m1 = Matrix(m1_height, m1_length)
    m1.fill()
    res_matrix = m1.transpose(n)
    print("The result is:")
    res_matrix.show()


def get_choice():
    return int(input("""
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
0. Exit
Your choice: """.lstrip()))


def show_err():
    print("The operation cannot be performed.")


def execute(choice):
    if choice == 1:
        add_matrices()
    elif choice == 2:
        mul_by_const()
    elif choice == 3:
        mul_by_matrix()
    elif choice == 4:
        transpose_matrix()
    return


while True:
    choice = get_choice()
    if choice == 0:
        break
    execute(choice)
    print()
