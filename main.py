# Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента
# функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Если строк меньше двух, выдайте текст ОШИБКА! Размерности таблицы должны быть больше 2!.
#
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
# Пример
# На входе:
def print_operation_table(operation, num_rows, num_columns):

    if num_rows > 2 and num_columns > 2:
        table = []
        table.append([y for y in range(1, num_columns + 1)])
        for x in range(2, num_rows + 1):
            line = []
            line.append(x)
            for y in range(2, num_columns + 1):
                line.append(operation(x, y))
            table.append(line)

        for i in table:
            print(' '.join(list(map(str, i))))
    else:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")


print_operation_table(lambda x, y: x * y)

# На выходе:

# 1 2 3
# 2 4 6
# 3 6 9



