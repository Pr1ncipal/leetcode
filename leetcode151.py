class Solution:
    def reverseWords(self, s: str) -> str:
        # check for leading/trailing whitespace
        if s[0] == ' ':
            s = s[1:]
        if s[-1] == ' ':
            s = s[:-1]

        # check for duplicate spaces
        i = 0
        while i < len(s):
            print(s[i])
            if s[i] != s[-1] and s[i] == ' ' and s[i+1] == ' ':
                s = s[:i] + s[i+1:]
            i += 1

        # split string into an array, return the reversed list
        strArray = s.split()
        return ' '.join(strArray[::-1])

# Ended up using while loops to deal with the changing string length as spaces are removed. O(n) time complexity + 2 for leading/trailing whitespace check
