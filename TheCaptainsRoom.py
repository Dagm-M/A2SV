# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

sizeOfFamilies = int(input())

peoples = map(int, input().split())

peoples = Counter(peoples)

for key,value in peoples.items():
    if value == 1:
        print(key)
        exit()
