def run(pdata: dict) -> dict:
    # TODO

    avg_data = {}
    world_population = sum(list(pdata.values()))

    for city, population in pdata.items():
        avg_data[city] = round(population * 100 / world_population, 3)

    return avg_data

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
