def run(fullname: str) -> str:
    # TODO
    surname, name = [part.strip() for part in fullname.split(',')]

    name_initial = name.split()[0][0].upper()

    surname_parts = surname.split()
    surname_initials = '.'.join(word[0].upper() for word in surname_parts)

    initials = f'{name_initial}.{surname_initials}.'

    return initials


"""
Another version

def run(fullname: str) -> str:

    formatted_fullname = fullname.split()

    if len(formatted_fullname) == 2:
        name_initial = formatted_fullname[1][0]
        surname_initials = formatted_fullname[0][0]
    else:
        name_initial = formatted_fullname[2][0]
        surname_initials = f'{formatted_fullname[0][0]}.{formatted_fullname[1][0]}'

    initials = f'{name_initial.upper()}.{surname_initials.upper()}.'
    return initials
"""


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
