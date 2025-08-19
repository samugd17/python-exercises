def run():
    # TODO
    n = 0
    for i in range(7):
        for u in range(n, 7):
            print(f'{i}|{u}', end=' ')
        print()
        n += 1


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
