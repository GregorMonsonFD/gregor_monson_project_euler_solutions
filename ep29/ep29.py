
def power_loop(lower_bound : int, upper_bound : int):
    a = lower_bound
    b = upper_bound

    distinct_results = []

    for i in range(a, b + 1):
        for j in range(a, b + 1):
            result = pow(i, j)

            if result not in distinct_results:
                distinct_results.append(result)

    return distinct_results


def main():
    results  = power_loop(2, 100)

    print(f"Number of distinct items is : {len(results)}")


if __name__ == '__main__':
    main()