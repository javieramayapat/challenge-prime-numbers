import math


def get_primes(number_of_primes_to_get):
    if number_of_primes_to_get < 1:
        raise ValueError("Number of primes must be a positive number grather tha 1")

    if type(number_of_primes_to_get) not in [int]:
        raise TypeError("Number ust be a positive integer")

    primes_list = []
    counter_primes = 0
    serial_number = 2

    while counter_primes < number_of_primes_to_get:
        is_prime = True

        for number in range(2, int(math.sqrt(serial_number)) + 1):
            if serial_number % number == 0:
                is_prime = False
                break

        if is_prime:
            primes_list.append(serial_number)
            counter_primes += 1

        serial_number += 1

    return primes_list


def run():
    test_1 = 6
    result = get_primes(test_1)
    print(f"List of primes: {result}")


if __name__ == "__main__":
    run()
