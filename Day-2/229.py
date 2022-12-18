class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = {}
        limit = len(nums)//3
        print(limit)
        res =[]
        for n in nums:
            if n not in dic:
                dic[n] = 0
            dic[n] += 1
        val = list(dic.values())
        keys = list(dic.keys())
        print(val)
        print(keys)
        for i in range(len(val)):
            if val[i]>limit:
                res.append(keys[i])
        return (res)