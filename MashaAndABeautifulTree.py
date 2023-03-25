def main():
    n = int(input())

    for test in range(n):
        size = int(input())
        nums = list(map(int, input().split()))
        newNums = []
        counter = 0

        i = 0
        isIn = False
        while i < len(nums)-1:
            if abs(nums[i] - nums[i+1]) != 1:
                print(-1)
                isIn = True
                break
            if nums[i] < nums[i+1]:
                newNums.append([nums[i], nums[i+1]])
            else:
                newNums.append([nums[i+1], nums[i]])
                counter += 1
            i += 2

        if isIn:
            continue

        if len(newNums) == 0:
            print(0)
            continue

        val = sort(newNums, 0, len(newNums)-1)
        if val == -1:
            print(val)
            continue

        print(val + counter)


def sort(nums, left, right):
    if left == right:
        return 0

    mid = left + (right - left)//2

    firstHalf = sort(nums, left, mid)
    if firstHalf == -1:
        return firstHalf
    secondHalf = sort(nums, mid+1, right)
    if secondHalf == -1:
        return secondHalf

    now = 0
    if nums[left][0] > nums[mid+1][0]:
        now = 1
        nums[left:mid+1], nums[mid+1:right +
                               1] = nums[mid+1:right + 1], nums[left:mid+1]

    if abs(nums[mid][1] - nums[mid+1][0]) != 1:
        return -1

    return firstHalf + secondHalf + now


main()
