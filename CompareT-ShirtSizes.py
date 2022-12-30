def printSign(left, right):
    if left > right:
        print(">")
    elif right > left:
        print("<")
    else:
        print("=")


testCases = int(input())
sizes = []

for num in range(testCases):
    temp = input().split()
    for size in temp:
        if size == "M":
            sizes.append(0)
        else:
            index = len(size) - 1
            start = -10 if size[index] == "S" else 10
            while index >= 0:
                if start < 0:
                    start -= 1
                else:
                    start += 1
                index -= 1
            sizes.append(start)

index = 0
while index < len(sizes):
    printSign(sizes[index], sizes[index+1])
    index += 2
