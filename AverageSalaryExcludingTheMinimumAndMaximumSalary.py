class Solution:
    def average(self, salary: List[int]) -> float:
        sum = 0
        minimum = salary[0]
        maximum = salary[1]
        for salar in salary:
            minimum = min(minimum, salar)
            maximum = max(maximum, salar)
            sum += salar

        return (sum - minimum - maximum)/(len(salary) -2)

    
