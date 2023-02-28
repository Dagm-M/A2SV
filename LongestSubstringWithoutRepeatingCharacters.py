class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        size = 0
        left = 0

        for right in range(len(s)):

            while left <= right and s[right] in unique:
                unique.remove(s[left])
                left += 1

            unique.add(s[right])
            size = max(size, right - left + 1)
            
        return size
