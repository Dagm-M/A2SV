class TopVotedCandidate:
    arr = []
    def __init__(self, persons: List[int], times: List[int]):
        frequency = defaultdict(int)
        arr = []
        mostFrequent = [persons[0],1]
        for i in range(len(persons)):
            frequency[persons[i]] += 1

            if frequency[persons[i]] >= mostFrequent[1]:
                mostFrequent = [persons[i], frequency[persons[i]]]

            arr.append([times[i], mostFrequent[0]])

        self.arr = arr

    def q(self, t: int) -> int:
        left = 0
        right = len(self.arr) - 1
        ans = 0

        while left <= right:
            mid = left + (right - left)//2

            if self.arr[mid][0] == t:
                ans = mid
                break
            elif self.arr[mid][0] > t:
                right = mid -1
            else:
                ans = mid
                left = mid + 1

        return self.arr[ans][1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
