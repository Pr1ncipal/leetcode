# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        minimum = 1
        maximum = n
        guesser = n // 2
        check = 2
        while minimum <= maximum:
            guesser = (minimum + maximum) // 2
            result = guess(guesser)
            if result == 0:
                return guesser
            elif result == -1:
                maximum = guesser - 1
            else:
                minimum = guesser + 1

# This one was more difficult than it should have been. I ran into an issue with rounding as well as what I used for the while loop, but after a bit of research I figured out what I did wrong.
