class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        sdict = {}
        tdict = {}

        for letter in s:
            if letter in sdict:
                sdict[letter] += 1
            else:
                sdict[letter] = 1
        
        for letter in t:
            if letter in tdict:
                tdict[letter] += 1
            else:
                tdict[letter] = 1
        
        if tdict == sdict:
            return True
            
        return False