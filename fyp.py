def new_even_or_odd(minimum, maximum, category):
    odd_list = [number for number in range(minimum, maximum + 1) if number % 2 != 0]
    even_list = [number for number in range(minimum, maximum + 1) if number % 2 == 0]
    if category == 'even':
        return len(even_list)
    elif category == 'odd':
        return len(odd_list)
    else:
        return None

print(new_even_or_odd(2, 10, 'even'))
