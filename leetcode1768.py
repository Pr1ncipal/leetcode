# Leetcode 1768 - Merge Strings Alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedWord = ""
        runtime = 200
        for counter in range(0, runtime):
            if counter % 2 == 0 and len(word1) > 0:
                mergedWord = mergedWord + word1[0]
                word1 = word1[1:]
            if counter % 2 == 1 and len(word2) > 0:
                mergedWord = mergedWord + word2[0]
                word2 = word2[1:]
        return mergedWord

'''
Comments:
I think I could do this more efficiently. Using 200 as a preset amount of times to loop works, however only because in this scenario because I know the length of both strings is at the most 200 characters.
'''
