with (
    open('input', 'r', encoding='utf-8') as f_in,
    open('output', 'w', encoding='utf-8') as f_out
):
    for line in f_in:
        if line.strip() != '100':
            f_out.write(line)
