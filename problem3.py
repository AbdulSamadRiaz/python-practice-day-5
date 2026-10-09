def sum_num(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
    
numbers = [10,20,30,40]
print(sum_num(numbers))