import sys

def circular_path(n, m):
    array = [i + 1 for i in range(n)]
    path = []
    current_index = 0
    
    while True:
        path.append(array[current_index])
        current_index = (current_index + m) % n
        if current_index == 0:
            break
    
    return ''.join(map(str, path))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python script.py n m")
    else:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        result = circular_path(n, m)
        print(result)
