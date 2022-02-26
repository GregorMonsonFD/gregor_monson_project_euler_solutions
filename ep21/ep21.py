def find_divisors(x: int):
    divisor_list = []

    for i in range(1, x):
        if x % i == 0:
            divisor_list.append(i)

    return divisor_list


def check_is_amicable(a: int):
    a_divisors = find_divisors(a)
    b = sum(a_divisors)

    b_divisors = find_divisors(b)
    b_sum = sum(b_divisors)

    if a == b_sum:
        if a != b:
            return {'amicable': True, 'a': a, 'b': b}
        else:
            return {'amicable': False, 'a': a, 'b': b}
    else:
        return {'amicable': False, 'a': a, 'b': b}


def find_all_amicable():
    amicable_numbers = []
    non_amicable_numbers = []

    for i in range(1, 10000):
        if i in amicable_numbers or i in non_amicable_numbers:
            pass
        else:
            x = check_is_amicable(i)

            if x['amicable']:
                amicable_numbers.append(x['a'])
                amicable_numbers.append(x['b'])

                print(x)

            else:
                non_amicable_numbers.append(x['a'])
                non_amicable_numbers.append(x['b'])

    print(amicable_numbers)

    print("Sum of amicable numbers is : {}".format(sum(amicable_numbers)))


def main():
    find_all_amicable()


if __name__ == '__main__':
    main()
