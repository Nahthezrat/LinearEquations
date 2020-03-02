import math
import LinearEquations

# Начальные данные
N = 13
matrix_a = [
    [10.0*N+1, 4.0, 2.0, 2.0],
    [4.0, 8.0, 0.0, 2.0],
    [2.0, 0.0, 9.0, -4.0],
    [2.0, 2.0, -4.0, 12.0]
]
vector_b = [
    2.0*N*math.sin(N),
    5.0*(math.sin(N)-math.cos(N)),
    7.0*(math.sin(N)+math.cos(N)),
    3.0*math.sin(N)]


# Выводим систему (эхо-вывод)
for row in range(len(vector_b)):
    print("(", end='')
    for col in range(len(matrix_a[row])):
        print("\t{1:10.4f}{0}".format(" ", matrix_a[row][col]), end='')
    print("\t) * (\tX{0}) = (\t{1:10.4f})".format(row+1, vector_b[row]))

# Решаем систему
vector_x = LinearEquations.gauss(matrix_a, vector_b)

# Выводим решение
print("\n".join("X{0} =\t{1:10.4f}".format(i+1, x) for i, x in enumerate(vector_x)))
