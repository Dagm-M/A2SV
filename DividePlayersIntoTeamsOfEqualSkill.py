class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        totalSkill = skill[0] + skill[-1]
        chemistry = 0

        left = 0
        right = len(skill) - 1

        while left < right:
            if skill[left] + skill[right] != totalSkill:
                return -1
            
            chemistry += (skill[left] * skill[right])
            left += 1
            right -= 1

        return chemistry
