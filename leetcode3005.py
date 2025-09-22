class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        holder = [0] * 100
        for element in nums:
            holder[(element - 1)] += 1
        
        maxi = 0
        for item in holder:
            if item >= maxi:
                maxi = item 

        counter = 0
        for thing in holder:
            if thing == maxi:
                counter += thing
        return counter

# 3 pass solution. Other solutions had 1 pass, however this solution was also <2ms. Could def. be done cleaner/more optimally though.
