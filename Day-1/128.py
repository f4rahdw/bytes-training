#Longest Commmon Sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        val=0
        nums = set(nums)

        for num in nums:
            if num-1 not in nums:
                streak = num+1
                while streak in nums:
                    streak+=1
                val = max(val,streak-num)
        return val 