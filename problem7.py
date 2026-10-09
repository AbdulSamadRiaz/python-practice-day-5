def get_even_num(numbers):

    even_num = []

    for num in numbers:
        if num % 2== 0:
            even_num.append(num)

    return even_num

numbers = [10,15,22,31,40,55,68,71]
even_num = get_even_num(numbers)
print(even_num)

