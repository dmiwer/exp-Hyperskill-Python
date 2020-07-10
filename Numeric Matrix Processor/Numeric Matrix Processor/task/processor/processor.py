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

    @staticmethod
    def cof(row, col, arr):
        m = []
        for j in range(len(arr)):
            if j == row: continue
            t = []
            for i in range(len(arr[0])):
                if i == col: continue
                t.append(arr[j][i])
            m.append(t)
        ans = Matrix.det(m)
        return ans if (row + col) % 2 == 0 else -ans

    @staticmethod
    def det(arr):
        if len(arr) == 2:
            return arr[0][0] * arr[1][1] - arr[0][1] * arr[1][0]
        return sum([arr[0][i] * Matrix.cof(0, i, arr) for i in range(len(arr[0]))])

    def show(self, formatted=False):
        def format(n):
            if n % 1 == 0: return int(n)
            return int(n * 100) / 100.0
        if formatted:
            for i in range(self.height):
                for j in range(self.length):
                    print(f"{format(self.arr[i][j]): >8}", end="")
                print()
        else:
            for i in range(self.height):
                print(*[self.arr[i][j] for j in range(self.length)])

    def fill(self):
        temp = []
        for i in range(self.height):
            t = list(map(float, input().split(" ")))
            if len(t) != self.length:
                return -1
            temp.append(t)
        self.arr = temp

    def sum(self, other):
        return Matrix.get(
            [[(self.arr[i][j] + other.arr[i][j]) for j in range(self.length)] for i in range(self.height)])

    def mul(self, other):
        if type(other) == type(2.3):
            return Matrix.get([[(self.arr[i][j] * other) for j in range(self.length)] for i in range(self.height)])
        elif type(other) == type(self):
            return Matrix.get(
                [[sum(self.arr[i][x] * other.arr[x][j] for x in range(self.length)) for j in range(other.length)] for i
                 in range(self.height)])
        else:
            return -1

    def transpose(self, n=1):
        if n == 1:
            return Matrix.get([[self.arr[j][i] for j in range(self.length)] for i in range(self.height)])
        elif n == 2:
            return Matrix.get(
                [[self.arr[j][i] for j in reversed(range(self.length))] for i in reversed(range(self.height))])
        elif n == 3:
            return Matrix.get([[self.arr[i][j] for j in reversed(range(self.length))] for i in range(self.height)])
        elif n == 4:
            return Matrix.get([[self.arr[i][j] for j in range(self.length)] for i in reversed(range(self.height))])
        else:
            return -1

    def determinant(self):
        if self.height == 0: return 0
        if self.height == 1: return self.arr[0][0]
        return Matrix.det(self.arr)

    def inverse(self):
        d = self.determinant()
        if d == 0:
            return -1
        c = Matrix.get([[Matrix.cof(h, l, self.arr) for l in range(self.length)] for h in range(self.height)])
        return c.transpose().mul(1.0/d)


def add_matrices():
    m1_height, m1_length = map(int, input("Enter size of first matrix: ").split(" "))
    print("Enter first matrix: ")
    m1 = Matrix(m1_height, m1_length)
    m1.fill()
    m2_height, m2_length = map(int, input("Enter size of second matrix: ").split(" "))
    if m1_height != m2_height or m1_length != m2_length:
        show_err()
        return
    print("Enter second matrix: ")
    m2 = Matrix(m2_height, m2_length)
    m2.fill()
    print("The result is:")
    res_matrix = m1.sum(m2)
    res_matrix.show()


def mul_by_matrix():
    m1_height, m1_length = map(int, input("Enter size of first matrix: ").split(" "))
    print("Enter first matrix: ")
    m1 = Matrix(m1_height, m1_length)
    m1.fill()
    m2_height, m2_length = map(int, input("Enter size of second matrix: ").split(" "))
    if m1_length != m2_height:
        show_err()
        return
    print("Enter second matrix: ")
    m2 = Matrix(m2_height, m2_length)
    m2.fill()
    print("The result is:")
    res_matrix = m1.mul(m2)
    res_matrix.show()


def mul_by_const():
    m1_height, m1_length = map(int, input("Enter size of first matrix: ").split(" "))
    print("Enter matrix: ")
    m1 = Matrix(m1_height, m1_length)
    m1.fill()
    c = float(input("Enter constant: "))
    print("The result is:")
    res_matrix = m1.mul(c)
    res_matrix.show()


def calc_det():
    m1_height, m1_length = map(int, input("Enter matrix size: ").split(" "))
    m1 = Matrix(m1_height, m1_length)
    if m1_height != m1_length:
        show_err()
        return
    print("Enter matrix: ")
    m1.fill()
    print("The result is: ")
    result = m1.determinant()
    print(result)


def inverse():
    m1_height, m1_length = map(int, input("Enter matrix size: ").split(" "))
    m1 = Matrix(m1_height, m1_length)
    print("Enter matrix: ")
    m1.fill()
    res_matrix = m1.inverse()
    if type(res_matrix) == int:
        print("The matrix doesn't have an inverse.")
    elif type(res_matrix) == Matrix:
        print("The result is: ")
        res_matrix.show()


def show_err():
    print("The operation cannot be performed.")


def transpose_matrix():
    n = int(input("""
1. Main diagonal
2. Said diagonal
3. Vertical line
4. Horizontal line
Your choice: > """))
    m1_height, m1_length = map(int, input("Enter matrix size: ").split(" "))
    print("Enter matrix: ")
    m1 = Matrix(m1_height, m1_length)
    m1.fill()
    print("The result is:")
    res_matrix = m1.transpose(n)
    res_matrix.show()


while True:
    choice = int(input("""
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit
Your choice: """.lstrip()))
    if choice == 0:     break
    elif choice == 1:   add_matrices()
    elif choice == 2:   mul_by_const()
    elif choice == 3:   mul_by_matrix()
    elif choice == 4:   transpose_matrix()
    elif choice == 5:   calc_det()
    elif choice == 6:   inverse()
    print()
