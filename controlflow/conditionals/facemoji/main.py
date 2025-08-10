def run(feeling: str) -> str:
    # TODO

    match feeling.title():
        case 'Happy':
            emoji = '😀'
        case 'Sad':
            emoji = '😔'
        case 'Angry':
            emoji = '😡'
        case 'Pensive':
            emoji = '🤔'
        case 'Surprised':
            emoji = '😮'
        case _:
            emoji = None

    return emoji


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
