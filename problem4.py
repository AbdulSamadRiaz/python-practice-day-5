def largest_num(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
numbers = [123,342,309,345,543,233,333]
result = largest_num(numbers)
print(result)



def smallest_num(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest
numbers = [123,342,309,345,543,233,333]
result = smallest_num(numbers)
print(result)