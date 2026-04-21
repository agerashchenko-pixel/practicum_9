import os


os.makedirs('simple', exist_ok=True)
output_path = os.path.join('simple', 'output')

with (
    open('input', 'r', encoding='utf-8') as f_in,
    open(output_path, 'w', encoding='utf-8') as f_out
):
    for i, line in enumerate(f_in, start=1):
        if i % 2 == 0:
            f_out.write(line)
