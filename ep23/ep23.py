def find_divisors(x: int):
    divisor_list = []

    for i in range(1, x):
        if x % i == 0:
            divisor_list.append(i)

    return divisor_list


def get_divisor_sum(x: int):
    divisors: list = find_divisors(x)
    sum_of_divisors: int = 0

    for divisor in divisors:
        sum_of_divisors += divisor

    return sum_of_divisors


def test_abundant(x: int):
    divisor_sum = get_divisor_sum(x)

    if divisor_sum > x:
        return {'is_abundant': True, 'divisor_sum': divisor_sum}
    else:
        return {'is_abundant': False, 'divisor_sum': divisor_sum}


def obtain_abundant_list():
    abundant_list = []

    for i in range(1, 28123):
        result = test_abundant(i)

        if result['is_abundant']:
            abundant_list.append(i)

    print(f'ePiC! Number of abundant numbers found : {len(abundant_list)}')

    return abundant_list


def find_non_abundant_sums():
    abundant_list = obtain_abundant_list()
    list_of_sums = []

    for i in range(len(abundant_list)):
        for j in range(i, len(abundant_list)):
            list_of_sums.append(abundant_list[i] + abundant_list[j])

    print("Non-abundant sum pairs found.")

    return list_of_sums


def find_non_compliance():
    list_of_sums = find_non_abundant_sums()
    summation = 0

    for i in range(28125):
        if i not in list_of_sums:
            print(f"{i} does not comply")
            summation += i

    print(f"Total of non compliance is {summation}")


def main():
    find_non_compliance()


if __name__ == '__main__':
    main()
