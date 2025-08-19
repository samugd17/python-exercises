def run(text):
    # TODO
    VOWELS = 'aeiouéáóí'
    num_vowels = 0
    for vowel in text:
        if vowel.lower() in VOWELS:
            num_vowels += 1
    return num_vowels


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
