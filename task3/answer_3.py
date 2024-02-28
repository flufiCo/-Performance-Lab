import json
import sys
import os


def read_json_file(file_name):
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Файл {file_name} не найден.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Ошибка при декодировании JSON в файле {file_name}.")
        sys.exit(1)


def update_report_values(report, values):
    for test_id, test_data in report.items():
        if "tests" in test_data:
            update_report_values(test_data["tests"], values)
        elif test_id in values:
            test_data["value"] = values[test_id]


def write_json_file(data, file_name):
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
        print(f"Файл {file_name} успешно создан.")
    except IOError:
        print(f"Ошибка при записи в файл {file_name}.")
        sys.exit(1)


if __name__ == "__main__":
    values_file = "values.json"
    tests_file = "tests.json"
    report_file = "report.json"

    values_data = read_json_file(values_file)
    tests_data = read_json_file(tests_file)

    update_report_values(tests_data, values_data)

    write_json_file(tests_data, report_file)
