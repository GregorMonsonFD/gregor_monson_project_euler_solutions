
def power_sum(base: int, exponent: int):
    digit_sum: int = 0
    exponent_result: int = pow(base, exponent)
    exponent_result_string: str = str(exponent_result)

    for i in range(len(str(exponent_result))):
        digit_sum += int(exponent_result_string[i])

    return digit_sum


def main():
    print(power_sum(2, 1000))


if __name__ == '__main__':
    main()
