class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        words = text.split(' ')
        flag = False
        counter = 0
        for word in words:
            for letter in word:
                if letter in brokenLetters:
                    flag = True
                    break
            if flag == False:
                counter += 1
            flag = False
        return counter

# Finished this on my second try in < 3 minutes, which I'm pretty proud of. Only forgot a colon on the second if statement.
