class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        sdict = {}
        for letter in s:
            if letter in sdict.keys():
                sdict[letter] += 1
            else:
                sdict[letter] = 1
        
        for letter in t:
            if letter in sdict.keys():
                sdict[letter] -= 1
            else:
                return False
        
        for value in sdict.values():
            if value != 0:
                return False

        return True