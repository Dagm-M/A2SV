class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        M = [0] * n
        
        for i in range(n-1,-1,-1):
            if i + questions[i][1] + 1 < n:
                M[i] = max(questions[i][0] + M[i + questions[i][1] + 1], M[i + 1])
                
            elif i +1 < n:
                M[i] = max(questions[i][0], M[i + 1])
    
            else:
                M[i] = questions[i][0]
        
        return M[0]
