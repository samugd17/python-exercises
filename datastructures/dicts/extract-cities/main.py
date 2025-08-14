def run(cinfo: str) -> dict:
    # TODO

    cities = {}

    formatted_cinfo = cinfo.split(';')
    for e in formatted_cinfo:
        city, population = e.split(':')
        cities[city] = int(population.replace('_', ''))

    return cities


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
