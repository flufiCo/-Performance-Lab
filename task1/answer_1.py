import sys


def circular_path(n, m):
    circle = list(range(1, n + 1))
    path = []

    current_position = 0
    for _ in range(n // m):
        current_interval = circle[current_position:current_position + m]

        path.append(current_interval[0])
        current_position = (current_position + m) % n

    return path


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python script.py <n> <m>")
        sys.exit(1)

    n = int(sys.argv[1])
    m = int(sys.argv[2])

    result_path = circular_path(n, m)
    print("Круговой массив:", ''.join(map(str, range(1, n + 1))))
    print(f"При длине обхода {m} получаем интервалы:", end=" ")

    intervals = [result_path[i:i+m] for i in range(0, len(result_path), m)]
    for interval in intervals:
        print("".join(map(str, interval)), end=", ")

    print("\nПолученный путь:", ''.join(map(str, result_path)))
