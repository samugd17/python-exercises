# TODO


def factorial(n: int) -> int:
    if n < 0:
        return None
    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(factorial)
