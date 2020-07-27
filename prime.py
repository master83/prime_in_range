def run():
    try:
        num = input('Enter a numeric number: ')
        print(f'prime numbers lower than {num}: {calculate_prime_in_range(int(float(num)))}')
    except ValueError as verr:
        print('please enter integer value')
    except Exception as ex:
        print('invalid input')


def calculate_prime_in_range(max_range):
    if max_range <= 1:
        return []
    return [n for n in range(2, max_range) if all(n % i != 0 for i in range(2, n))]


if __name__ == '__main__':
    run()