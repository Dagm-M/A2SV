class Solution:
    def compress(self, chars: List[str]) -> int:

        first = 0
        second = 0
        size = 0

        while second < len(chars):
            if chars[first] != chars[second]:
                if second - first > 1:
                    length = str(second - first)
                    for c in length:
                        first += 1
                        chars[first] = c
                        size += 1
        
                size += 1

                first += 1
                while first != second:
                    chars[first] = ""
                    first += 1

            second += 1

        if second - first > 1:
            length = str(second - first)
            for c in length:
                first += 1
                chars[first] = c
                size += 1

        size += 1
        
        left = 0
        right = 0

        while right < len(chars):
            if chars[right] != "":
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
    
            right += 1

        return size
