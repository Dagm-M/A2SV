class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        
        l = len(s)
        k = len(p)
        p_counter = defaultdict(int)
        s_counter = defaultdict(int)
        count = []
        
        
        for i in p :
            p_counter[i]+=1
        right = 0 
        left = 0
        if l < k:
            return []
        while right < k :
            s_counter[s[right]]  += 1
            right+=1
            if s_counter == p_counter:
                count.append(left)
        
        while right < l:
            s_counter[s[right]]+=1
            s_counter[s[left]] -= 1
            if  s_counter[s[left]] == 0:
                del  s_counter[s[left]]

            left+=1 
            if s_counter == p_counter:
                count.append(left)
               
            right+=1 
           
        return count
