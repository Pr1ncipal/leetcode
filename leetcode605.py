class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        maxFlowers = 0
        # check 1 element array
        if len(flowerbed) == 1 and flowerbed[0] == 0 and n <= 1:
            return True
        elif len(flowerbed) == 1 and flowerbed[0] == 0 and n > 1:
            return False

        for i in range(len(flowerbed)):
            # check first element
            if i == 0 and flowerbed[i] != 1 and flowerbed[i + 1] != 1:
                flowerbed[i] = 1
                maxFlowers += 1

            # check last element
            if i == (len(flowerbed) - 1) and flowerbed[i] != 1 and flowerbed[i - 1] != 1:
                flowerbed[i] = 1
                maxFlowers += 1

            # check every other element
            elif flowerbed[i] != 1 and flowerbed[i - 1] != 1 and flowerbed[i + 1] != 1:
                flowerbed[i] = 1
                maxFlowers += 1

        if n <= maxFlowers:
            return True
        else:
            return False

# Not the most efficient way to solve this problem, but it works. In my opinion, more readable than other solutions that have 5+ checks in their if statements.
