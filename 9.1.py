with open('input', 'r', encoding='utf-8') as f_in:
    data = f_in.read()

with open('output', 'w', encoding='utf-8') as f_out:
    f_out.write(data.upper())
