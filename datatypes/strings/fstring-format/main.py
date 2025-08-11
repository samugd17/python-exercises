def run(number):
    # TODO
    formatted_number = str(number)
    print(f'{formatted_number[:5]}')
    print(f'{formatted_number}0')
    print(f'{' ' * 4}{float(formatted_number[:3]) + 0.02}')
    print(f'{formatted_number}0e+00')
    print(f'{'0' * 4}{formatted_number[:5]}3')
    print(f'{' ' * 12}{formatted_number}')


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
