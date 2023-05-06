class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequent_words = Counter(words)
        f_words = []
        ans = []
        for key,val in frequent_words.items():
            f_words.append([-1* val,key])

        heapify(f_words)
        for i in range(k):
            ans.append(heappop(f_words)[1])

        return ans