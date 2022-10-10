def detectCapitalUse( word):
    """
    :type word: str
    :rtype: bool
    """
    c=0
    for i in range(len(word)):
        if 90>=ord(word[i])>64:
            print(ord(word[i]))
            print(True)
            c+=1
    print(c)
    if c==len(word) or c==0:
        return True
    if c==1 and 90>=ord(word[0])>64:
        return True
    return False
print(detectCapitalUse("nF"))