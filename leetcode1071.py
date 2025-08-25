class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        denominator = gcd(len(str1), len(str2))
        list_of_repeats = [str1[i:i+denominator] for i in range(0, len(str1), denominator)]
        return list_of_repeats[0]

'''
Comments:
First problem I needed help for. Brute force works, but this uses a different solution checking that each string is truly a repeat of each other by first checking if both strings added together different ways equal each other. If it does, then all you need to find is the actual common denominator. I did this by finding the common denominator of the lengths of both strings, then using this (https://stackoverflow.com/questions/9475241/split-string-every-nth-character) method to split a string every nth character, and just returning the first iteration of such. Can probably be done more efficiently, bu this is my solution.
'''
