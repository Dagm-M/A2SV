class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        for i,task in enumerate(tasks):
            tasks[i].append(i)

        tasks.sort()
        heap = []
        time = tasks[0][0]
        ans = []

        i = 0
        while i < len(tasks):
            
            while i < len(tasks) and (not heap or tasks[i][0] <= time):
                heappush(heap, [tasks[i][1], tasks[i][2]])
                i += 1


            val = heappop(heap)
            ans.append(val[1])
            time += val[0]
            if not heap and i < len(tasks) and time < tasks[i][0]:
                time = tasks[i][0]

        while heap:
            val = heappop(heap)
            ans.append(val[1])


        return ans