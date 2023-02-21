testCases = int(input())


for test in range(testCases):
    size = int(input())

    nums = list(map(int, input().split()))

    maximum = nums[0]
    sum = 0
    curr = nums[0]

    for num in nums:

        if (num > 0 and curr < 0) or (num < 0 and curr > 0):
            sum += maximum
            maximum = num
        curr = num

        maximum = max(maximum, num)

    sum += maximum
    print(sum)
