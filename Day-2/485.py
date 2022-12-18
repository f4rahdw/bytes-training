class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        streak=0
        cstreak=0
        for n in nums:
            if n == 1:
                cstreak+=1
            else:
                streak = max(streak,cstreak)
                cstreak=0
            print(streak,cstreak)
        streak=max(streak,cstreak)
        return streak