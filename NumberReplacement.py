testCases = int(input())
size = []
nums = []
changed = []

for num in range(testCases):
    size.append(int(input()))
    nums.append(input().split())
    string = input()
    temp = []
    for char in string:
        temp.append(char)
    changed.append(temp)

for index in range(len(nums)):
    isNO = False
    numsWithChars = {}
    for char in range(size[index]):
        if nums[index][char] in numsWithChars.keys():
            if numsWithChars[nums[index][char]] != changed[index][char]:
                print("NO")
                isNO = True
                break
        else:
            numsWithChars[nums[index][char]] = changed[index][char]

    if not isNO:
        print("YES")
