def count_type(numbers):

    positive = 0
    negative = 0
    zero = 0

    for num in numbers:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zero += 1

    return positive,negative,zero

numbers = [10,-30,-1,0,90,0,98]
positive,negative,zero = count_type(numbers)
print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"Zero: {zero}")