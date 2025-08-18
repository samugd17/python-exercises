# TODO


def order_by_age(people_data: list[dict]) -> list[dict]:
    return sorted(people_data, key=lambda person: person['age'])


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(order_by_age)
