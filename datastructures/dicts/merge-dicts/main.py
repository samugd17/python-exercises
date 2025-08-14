def run(d1: dict, d2: dict) -> dict:
    # TODO
    
    """
        Optimal way to merge two dictionaries without modifying the originals.
        merged = d1 | d2
    """

    merged = d1.copy()  # Create a copy of d1 to avoid modifying the original

    for key, value in d2.items():
        if key not in d1:
            merged[key] = value
        else:
            merged[key] = value

    return merged


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
