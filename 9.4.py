with (open('input', 'r', encoding='utf-8') as f_in, 
        open('output', 'w', encoding='utf-8') as f_out):
    for line in f_in:
        if len(line.rstrip()) > 20:
            f_out.write(line)
