class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = Counter(s1)
        count = len(s1)
        left = 0
        
        for right in range(len(s2)):

            while left <= right and (s2[right] not in s1 or s1[s2[right]] <= 0):
                if s2[left] in s1:
                    if s1[s2[left]] == 0:
                        count += 1
                    s1[s2[left]] += 1
                left += 1
            
            if s2[right] in s1:
                s1[s2[right]] -= 1
                if s1[s2[right]] == 0:
                    count -= 1

            if count == 0:
                return True

        return False
