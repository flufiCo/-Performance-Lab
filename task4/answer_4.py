import sys

def min_moves_to_equal_elements(nums):
    # Сортируем массив
    nums.sort()
    
    # Находим медиану
    median = nums[len(nums) // 2]
    
    # Считаем количество шагов для приведения всех элементов к медиане
    moves = sum(abs(num - median) for num in nums)
    
    return moves

def read_nums_from_file(filename):
    try:
        with open(filename, 'r') as file:
            # Читаем и преобразуем все строки в числа
            nums = [int(line.strip()) for line in file.readlines()]
            print(f"Прочитанные числа: {nums}")
        return nums
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []

def main():
    if len(sys.argv) != 2:
        print("Использование: python script.py <input_file>")
        return
    
    # Читаем массив из файла
    filename = sys.argv[1]
    nums = read_nums_from_file(filename)
    
    if not nums:
        print("Ошибка: не удалось прочитать числа из файла.")
        return
    
    # Получаем минимальное количество ходов
    result = min_moves_to_equal_elements(nums)
    
    # Выводим результат
    print(f"Минимальное количество ходов: {result}")

if __name__ == "__main__":
    main()
