def player_movement(position, left_arrow, right_arrow, shift):
    if shift:
        step = 2
    else:
        step = 1

    if left_arrow:
        position -= step
    if right_arrow:
        position += step

    return position


print(player_movement(10, True, False, False))
print(player_movement(10, True, False, True))
print(player_movement(10, False, False, True))
print(player_movement(10, True, True, False))
