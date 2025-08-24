def run(target_x: int, target_y: int) -> int:
    # TODO
    x_move = 0
    y_move = 0
    movements = 0

    if not target_y and not target_x:
        return 0

    for i in range(1, target_x + 1):
        if i % 2 == 0:
            x_move += 1
            y_move += 2
        else:
            x_move += 2
            y_move += 1
        movements += 1
        if x_move == target_x and y_move == target_y:
            return movements
        if x_move > target_x or y_move > target_y:
            return -1


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
