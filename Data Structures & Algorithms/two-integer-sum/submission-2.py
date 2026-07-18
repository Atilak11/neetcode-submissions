class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num1 = 0
        num2 = 0
        arr = []
        find = {}

        for i in range(len(nums)):
            num1 = i
            if (target - nums[i]) in find:
                num2 = find[target - nums[i]]
                arr.append(num2)
                arr.append(num1)
                return arr
            find[nums[i]] = i

        return arr;