import random

def get_numbers_ticket(min_num, max_num, quantity):
    if not (1 <= min_num <= max_num <= 1000):
        return []
    if not (0 < quantity <= (max_num - min_num + 1)):
        return []
    unique_numbers = set()
    while len(unique_numbers) < quantity:
        unique_numbers.add(random.randint(min_num, max_num))
        sorted_numbers = sorted(unique_numbers)
    return sorted_numbers

lottery_numbers = get_numbers_ticket(1, 1000, 7)
print("Ваші лотерейні числа:", lottery_numbers)
