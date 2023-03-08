class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s) // 4
        minLength = inf
        counter = 0
        left = 0

        seen = {"Q":-n,"W":-n,"E":-n,"R":-n}
        for c in s:
            if c in seen:
                seen[c] += 1

        for c in ["Q","W","E","R"]:
            if seen[c] <= 0:
                del seen[c]
            else:
                counter += 1

        if counter == 0:
            return 0


        for right in range(len(s)):
            if s[right] in seen:
                seen[s[right]] -= 1
                if seen[s[right]] == 0:
                    counter -= 1

            while left <= right and counter <= 0:
                minLength = min(minLength,right - left + 1)

                if s[left] in seen:
                    seen[s[left]] += 1
                    if seen[s[left]] > 0:
                        counter += 1
                left += 1

        if minLength == inf:
            return 0

        return minLength
