somaPrimos = 0

for x in range (2, 10001):
    ndiv = 0

    for div in range (1, x+1):
        if x % div == 0:
            ndiv += 1

    if ndiv == 2:
        somaPrimos += x

print(f"A soma dos primos até 10.000 é {somaPrimos}.")