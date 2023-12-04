import re

def count_lines(log_file):
    with open(log_file, 'r') as file:
        lines = file.readlines()

    result = {}
    current_key = None

    for line in lines:
        search_match = re.search(r'Searching for occurrences of \'(.+?)\' in YAML3\.\.\.', line)
        if search_match:
            current_key = search_match.group(1)
            result[current_key] = 0
        elif current_key is not None:
            result[current_key] += 1

    return result

if __name__ == "__main__":
    log_file_path = "out"  # Replace with the actual path to your log file

    counts = count_lines(log_file_path)

    for key, value in counts.items():
        print(f"Search term '{key}': {value} lines below")

