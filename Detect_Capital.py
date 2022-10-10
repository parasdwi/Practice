class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        c=0
        for i in range(len(word)):
            if 90>=ord(word[i])>64:
                c+=1
        if c==len(word) or c==0 or (c==1 and 90>=ord(word[0])>64):
            return True
        return False