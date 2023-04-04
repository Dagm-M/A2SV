tests = int(input())

for x in range(tests):
    n = int(input())

    bits = list(str(bin(n))[2:])

    firstZero = -1
    total = 0

    for i in range(len(bits)-1, -1, -1):
        if bits[i] == "1":
            total += pow(2, len(bits) - i - 1)
            if firstZero > 0 and i == 0:
                total += pow(2, len(bits) - firstZero - 1)
            break

        if firstZero < 0 and bits[i] == "0":
            firstZero = i

    if firstZero < 0 and i == 0:
        total += pow(2, len(bits))

    print(total)
