from math import modf, sqrt

SCL = 5 << 22    # escala lineal
SCS = SCL * SCL    # escala superficial
small = 0
big = 0

for i in range(SCL // 2):
    y = i + 0.5
    low, high = modf(sqrt(SCS - y * y))
    small += low
    big += high

print("Pi= ", (small / SCS - sqrt(3) / 8 + big / SCS) * 12)
