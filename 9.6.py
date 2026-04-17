try:
    with open('input', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    if not lines:
        result = 'ERROR'
    else:
        count = int(lines[0].strip())
        real_lines_count = len(lines) - 1
        if real_lines_count == count:
            result = 'YES'
        else:
            result = 'NO'

except (ValueError):
    result = 'ERROR'

with open('output', 'w', encoding='utf-8') as file:
    file.write(result)

