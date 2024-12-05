x = 2
somaPrimos = 0

while x <= 10000:
    div = 1
    ndiv = 0
    while div <= x:
        if x % div == 0:
            ndiv += 1
        div += 1
    if ndiv == 2:
        somaPrimos += x
    x += 1
print(f"A soma dos primos até 10.000 é {somaPrimos}.")