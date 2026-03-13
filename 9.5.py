try:
    with open('input', 'r', encoding='utf-8') as f:
        nums = [line.strip() for line in f if line.strip()]
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
except FileNotFoundError:
    result = 'data error'
with open('output', 'w', encoding='utf-8') as f:
    f.write(result)
