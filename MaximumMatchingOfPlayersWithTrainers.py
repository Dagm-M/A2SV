class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        ptr1 = 0
        ptr2 = 0
        matchings = 0

        while ptr1 < len(players) and ptr2 < len(trainers):
            while ptr2 < len(trainers) and players[ptr1] > trainers[ptr2]:
                ptr2 += 1
            
            if ptr2 >= len(trainers):
                break

            matchings += 1
            ptr1 += 1
            ptr2 += 1

        return matchings
        
