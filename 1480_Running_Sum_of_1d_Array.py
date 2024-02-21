class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp = []
        for i in range(len(nums)):
            temp.append(sum(nums[0:i+1]))
        return temp
