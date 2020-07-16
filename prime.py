def run():
    num = input('Enter a numeric number: ')
    print(f'prime numbers lower than {num}: {calculate_prime_in_range(int(num))}')


def calculate_prime_in_range(max_range):
    prime_numbers = []
    if max_range <= 1:
        return []
    for num in range(2, max_range):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
        if is_prime:
            prime_numbers.append(num)
    return prime_numbers


if __name__ == '__main__':
    run()