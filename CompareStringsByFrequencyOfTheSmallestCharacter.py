class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        ans = []
        for i in range(len(words)):
            count = Counter(words[i])

            for j in range(97,123):
                if count[chr(j)] > 0:
                    words[i] = count[chr(j)]
                    break

        for i in range(len(queries)):
            count = Counter(queries[i])

            for j in range(97,123):
                if count[chr(j)] > 0:
                    queries[i] = count[chr(j)]
                    break

        words.sort()

        for querie in queries:
            pos = bisect_right(words,querie)
            ans.append(len(words) - pos)


        return ans
