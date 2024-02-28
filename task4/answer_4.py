def min_moves_to_equal(nums):
    total_moves = 0
    # Находим целевое число, к которому стремимся
    target = sum(nums) // len(nums)

    for num in nums:
        total_moves += abs(num - target)  # Считаем общее количество ходов

    return total_moves


if __name__ == "__main__":
    try:
        nums = [int(num)
                for num in input("Введите числа через пробел: ").split()]
    except ValueError:
        print("Неверный формат ввода. Введите целые числа через пробел.")
        exit(1)

    result = min_moves_to_equal(nums)
    print("Минимальное количество ходов:", result)
