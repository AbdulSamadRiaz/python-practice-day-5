def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count


numbers = [10, 15, 22, 31, 40, 55, 68]

result = count_even(numbers)

print(result)