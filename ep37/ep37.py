def check_prime(x: int):
    is_prime = True

    if x == 1:
        return False

    for i in range(2, x):
        if x % i == 0:
            is_prime = False
            break

    return is_prime


def find_truncations(x: int):
    truncations = [x]

    string_number = str(x)

    for i in range(1, len(string_number)):
        truncations.append(int(string_number[i:]))
        truncations.append(int(string_number[:-i]))

    return truncations


def main():
    i = 11
    truncatable_primes = []

    while True:
        prime_state = True
        for number in find_truncations(i):
            if not check_prime(number):
                prime_state = False
                break

        if prime_state:
            print(f"result found : {i}, {find_truncations(i)}")
            truncatable_primes.append(i)

        if len(truncatable_primes) == 11:
            break

        i += 2

    print(f"Sum of these is: {sum(truncatable_primes)}")


if __name__ == '__main__':
    main()