def check_brackets(sequence):
    counter = 0

    for char in sequence:
        if char == '(':
            counter += 1
        elif char == ')':
            counter -= 1

        if counter < 0:
            return False

    return counter == 0


print("Проверка скобочной последовательности")
print("1 - ввести с консоли")
print("2 - прочитать из файла")

choice = input("Выберите способ ввода (1 или 2): ")

if choice == "1":
    sequence = input("Введите скобочную последовательность: ")
elif choice == "2":
    filename = input("Введите имя файла: ")
    try:
        file = open(filename, 'r', encoding='utf-8')
        sequence = file.read().strip()
        file.close()
    except:
        print("Ошибка: файл не найден!")
        exit()
else:
    print("Неверный выбор!")
    exit()

if check_brackets(sequence):
    print("Правильная последовательность")
else:
    print("Неправильная последовательность")

