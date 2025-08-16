# TODO


def cfreq(elements: list, /, output_str: bool = False) -> list[tuple] | str:
    if not elements:
        return [] if not output_str else ''

    result = []
    actual = elements[0]
    counter = 1

    for element in elements[1:]:
        if element == actual:
            counter += 1
        else:
            result.append((actual, counter))
            actual = element
            counter = 1
    result.append((actual, counter))

    if output_str:
        return ','.join(f'{element}:{freq}' for element, freq in result)
    else:
        return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    cfreq([2, 2, 1, 1, 2, 2, 1, 1], False)
    # import vendor

    # vendor.launch(cfreq)
