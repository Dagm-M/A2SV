class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        adj = defaultdict(list)
        n = len(board) 
        num = 0
        sqr = n*n
        alternate = False
        Next = defaultdict(int)


        for i in range(n-1,-1,-1):

            for j in range(n):
                if alternate:
                    num -= 1
                else:
                    num += 1
                # print(num,end=" ")
                for z in range(num + 1, min(num + 7, sqr+1)):
                    adj[num].append(z)

                if board[i][j] != -1:
                    Next[num] = board[i][j]
                    
            # print()
            
            if alternate:
                num += (n-1)
            else:
                num += (n+1)
            alternate = not alternate

        q = deque()
        seen = set()
        q.append([1,0])
        # print(Next)
        
        while q:
            # print(q)
            val,length = q.popleft()
            # print(seen)

            for ad in adj[val]:
                if ad == sqr:
                    return length + 1
                if ad not in seen:
                    if ad in Next:
                        if Next[ad] == sqr:
                            return length + 1
                        q.append([Next[ad],length+1])
                    else:
                        q.append([ad,length+1])
                seen.add(ad)

        return -1