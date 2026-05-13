from math import sqrt


def pi():

    SCALE = 7 << 22
    RADIUS = SCALE
    R2 = RADIUS * RADIUS
    small = 0
    big = 0

    for i in range(RADIUS // 2):
        y = i + 0.5
        small += sqrt(R2 - y * y)
        if small >= RADIUS:
            small -= RADIUS
            big += RADIUS
    return (small / R2 - sqrt(3) / 8 + big / R2) * 12


print("Pi= ", pi())
