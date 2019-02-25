def new_even_or_odd(minimum, maximum, category):
    if category == 'even':
        return len([number for number in range(minimum, maximum + 1) if number % 2 == 0])
    elif category == 'odd':
        return len([number for number in range(minimum, maximum + 1) if number % 2 == 0])
    return None

print(new_even_or_odd(2, 10, 'even'))

# todo: Work this out
# even_counter = 0
# odd_counter = 0 
# loop while checking if num is even -> increment even_counter
# else loop while checking if num is odd -> increment odd_counter
