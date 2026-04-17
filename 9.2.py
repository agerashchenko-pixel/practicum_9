with (open('input', 'r', encoding='utf-8') as f_in,
      open('output', 'w', encoding='utf-8') as f_out):
    for line in f_in:
        if line.startswith(('A', 'a')):
            f_out.write(line)
