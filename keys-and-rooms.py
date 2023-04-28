class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque()
        seen = set()

        def inqueue(nums):
            for num in nums:
                if num not in seen:
                    q.append(num)
                
        inqueue(rooms[0])
        seen.add(0)

        while q:
            val = q.popleft()
            if val not in seen:
                inqueue(rooms[val])
            seen.add(val)

        return len(seen) == len(rooms)