import math


def factorial_sum(x: int):
    factorial_sum_total = 0
    total = math.factorial(x)
    total_string = str(total)

    for i in range(len(total_string)):
        factorial_sum_total += int(total_string[i])

    return factorial_sum_total


def main():
    print(factorial_sum(100))


if __name__ == '__main__':
    main()