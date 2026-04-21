with open('input', 'r', encoding='utf-8') as f_in:
    symbols = []
    for line in f_in:
        if line.strip():
            first_char = line[0]
            symbols.append(first_char)

    result = "".join(symbols)

with open('output', 'w', encoding='utf-8') as f_out:
    f_out.write(result)
