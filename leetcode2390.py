class Solution:
    def removeStars(self, s: str) -> str:
        for char in s:
            index = s.find('*')
            if index != -1:
                s = s[:(index-1)] + s[(index+1):]
        return s

# Not the fastest solution as this searches the entire string when the for loop iterates. Other solutions, however, utilize an array while this solution does all changes in place.
