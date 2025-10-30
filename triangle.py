def pascal_triangle(n):
    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]

        triangle.append(row)

    return triangle


while True:
    try:
        n = input("Введите количество строк треугольника Паскаля: ")
        n = int(n)
        if n <= 0:
            print("Ошибка: число должно быть положительным!")
            continue

        break
    except:
        print("Ошибка: введите целое число!")


triangle = pascal_triangle(n)

last_row = " ".join(str(num) for num in triangle[-1])
max_width = len(last_row)

print("\nТреугольник Паскаля:")
for row in triangle:
    row_string = " ".join(str(num) for num in row)

    spaces = (max_width - len(row_string)) // 2

    print(" " * spaces + row_string)

