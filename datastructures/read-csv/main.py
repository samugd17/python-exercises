def run(datafile: str) -> list:
    # TODO

    def check_values(value):
        if value.isdigit():
            return int(value)
        elif value == 'True':
            return True
        elif value == 'False':
            return False
        elif value == '':
            return None
        return value

    data = []

    with open(datafile, 'r') as f:
        keys = tuple(f.readline().strip().split(','))
        for line in f:
            values = line.strip().split(',')
            row = {key: check_values(value) for key, value in zip(keys, values)}
            data.append(row)

    return data


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    run('data/pokemon.csv')
    import vendor

    vendor.launch(run)
