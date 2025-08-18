def run(text: str) -> dict:
    # TODO
    
    """Using count()
    counter = {}
    for letter in text:
        counter[letter] = text.count(letter)
    return counter
    """

    counter = {}
    for letter in text:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
    return counter


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
