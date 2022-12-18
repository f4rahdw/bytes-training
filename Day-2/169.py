class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for n in nums:
            if n in dic:
                dic[n]+=1
            else:
                dic[n]=0
        res = max(dic,key= dic.get)
        return res
            
