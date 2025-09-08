class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = 0
        result = [None] * len(candies)

        for j in range(len(candies)):
            if candies[j] > maxCandies:
                maxCandies = candies[j]
        
        for i in range(len(candies)):
            candies[i] += extraCandies
            if candies[i] >= maxCandies:
                result[i] = True
            else:
                result[i] = False

        return result

# Came up with this first try, and beats 100% of all other times. Can be done with less lines using outside packages and other python tricks, but this is far more readable.
