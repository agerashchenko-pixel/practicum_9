try:
    with open('input', 'r', encoding='utf-8') as f:
        nums = []
        for line in f:
            nums.append(line.strip())
    if len(nums) < 3:
        result = 'data error'
    else:
        a = int(nums[0])
        b = int(nums[1])
        c = int(nums[2])
        result = str(a / b + c)

except ValueError:
    result = 'data error'
except ZeroDivisionError:
    result = 'division by 0'
with open('output', 'w', encoding='utf-8') as f:
    f.write(result)
