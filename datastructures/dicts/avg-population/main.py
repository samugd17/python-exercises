def run(pdata: dict) -> dict:
    # TODO

    avg_data = {}
    world_population = sum(list(pdata.values()))

    for city, population in pdata.items():
        avg_data[city] = round(population * 100 / world_population, 3)

    return avg_data

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    run({'Tokyo': 38140000, 'Delhi': 26454000, 'Shanghai': 24484000, 'Mumbai': 21357000})
    # import vendor

    # vendor.launch(run)
