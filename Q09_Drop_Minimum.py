def drop_minimum(*args):

    numbers = list(args)

    minimum = min(numbers)

    numbers.remove(minimum)

    return numbers


result = drop_minimum(5, -2, 8, 4, -5, 7, 10)

print(result)
