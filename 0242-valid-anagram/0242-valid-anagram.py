class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_s = {}
        dict_t = {}

        for char in s:
            if char not in dict_s:
                dict_s[char] = 1
            else: 
                dict_s[char] += 1
        
        for char in t:
            if char not in dict_t:
                dict_t[char] = 1
            else: 
                dict_t[char] += 1
        
        if dict_t == dict_s:
            return True
        else:
            return False