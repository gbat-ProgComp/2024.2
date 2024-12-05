x = 2
primos = 0

while x <= 10000:
    div = 1
    ndiv = 0
    while div <= x:
        if x % div == 0:
            ndiv += 1
        div += 1
    if ndiv == 2:
        primos += 1
    x += 1
print(f"São {primos} o tanto de primos até 10.000")