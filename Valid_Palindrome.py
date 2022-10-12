class Solution(object):
    def isPalindrome( self,s):
        i=0
        j=len(s)-1
        while i<j:
            while not self.alphanumeric(s[i]) and i<j:
                i+=1
            while not self.alphanumeric(s[j]) and j>i:
                j-=1
            if s[i].lower()!=s[j].lower():
                return False
            i+=1
            j-=1
        return True
    def alphanumeric(self, c):
        return (ord("A")<=ord(c)<=ord("Z")) or (ord("0")<=ord(c)<=ord("9")) or (ord("a")<=ord(c)<=ord("z"))
        
