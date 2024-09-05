import json
import sys

def fill_values(tests, values_dict):
    for test in tests:
        test_id = test['id']
        if test_id in values_dict:
            test['value'] = values_dict[test_id]
        
        if 'values' in test:
            fill_values(test['values'], values_dict)
    
def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <values.json> <tests.json> <report.json>")
        return

    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]

    with open(values_path, 'r') as f:
        values = json.load(f)

    with open(tests_path, 'r') as f:
        tests = json.load(f)

    # Создаем словарь для быстрого поиска значений по ID
    values_dict = {item['id']: item['value'] for item in values}

    # Заполняем значения в структуре tests.json
    fill_values(tests, values_dict)

    # Сохраняем результат в report.json
    with open(report_path, 'w') as f:
        json.dump(tests, f, indent=4)

if __name__ == "__main__":
    main()
