with open('input', 'r', encoding='utf-8') as f_in:
    result = "".join(line[0] for line in f_in if line.strip())
with open('output', 'w', encoding='utf-8') as f_out:
    f_out.write(result)
