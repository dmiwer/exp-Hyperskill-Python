ax, ay = [int(x) for x in input().split()]
m1 = [[int(y) for y in input().split()] for _ in range(ax)]

# bx, by = [int(x) for x in input().split()]
# m2 = [[int(y) for y in input().split()] for _ in range(bx)]
#
# if ax == bx and ay == by:
#     for x in range(ax):
#         print(" ".join(str(m1[x][y] + m2[x][y]) for y in range(ay)))
# else:
#     print("ERROR")

c = int(input())

for x in range(ax):
    print(*[m1[x][y] * c for y in range(ay)])
