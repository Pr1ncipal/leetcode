class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        lagging = 0
        leading = 1
        if len(nums) == 1:
            return 0
        while leading != len(nums) and lagging != len(nums):
            if nums[lagging] == 0 and nums[leading] != 0:
                temp = nums[lagging]
                nums[lagging] = nums[leading]
                nums[leading] = temp
            elif nums[lagging] == 0 and nums[leading] == 0:
                leading += 1
            elif nums[lagging] != 0 and nums[leading] != 0:
                lagging += 1
            elif nums[lagging] != 0 and nums[leading] == 0:
                leading += 1
                lagging += 1
            if lagging == leading:
                leading += 1        

# Took a minute, but got the submission in @ 8ms, beating ~85%. Starting to get a hang of the double pointer system. Readability for sure could be improved.
