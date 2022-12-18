class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        c,i = 0,0
        for j in range(len(nums)):
            if nums[i] != nums[j]:
                i+=1
                nums[i] = nums[j]
                c+=1
        return c+1