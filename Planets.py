from collections import Counter

testCases = int(input())
sizeAndCost = []
planets = []

for index in range(testCases):
    sizeAndCost.append(input().split())
    planets.append(Counter(input().split()))

# for a in planets:
#     print(a.keys())
#     print(a.values())


for index in range(testCases):
    sum = 0
    for vlaue in planets[index].values():
        if vlaue > int(sizeAndCost[index][1]):
            sum += int(sizeAndCost[index][1])
        else:
            sum += vlaue

    print(sum)
