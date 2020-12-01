"""
"""

def fibonacci():
    """
    Вычисление чисел Фибоначчи

    """

    # Определяем начальную последовательность Фибоначчи
    fib_1, fib_2 = 0, 1

    while True:
        yield fib_1
        # Вычисляем следующий элемент ряда Фибоначчи
        fib_1, fib_2 = fib_2, fib_1 + fib_2

def main():
    # Все числа
    # All Fibonacci numbers
    f = fibonacci()
    z = [x for (i, x) in zip(range(111), f)]
    print(z)

    # Чётные числа
    # Even Fibonacci numbers only
    f = fibonacci()
    z = [x for (i, x) in zip(range(111), f) if x % 2 == 0]
    print(z)

    # Нечётные числа
    # Odd Fibonacci numbers only
    f = fibonacci()
    z = [x for (i, x) in zip(range(111), f) if x % 2 != 0]
    print(z)

if __name__ == "__main__":
    main()
