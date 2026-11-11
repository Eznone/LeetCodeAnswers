class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        pos = 0

        res = ""

        while pos < len(word1) and pos < len(word2):
            res = res + word1[pos]
            res = res + word2[pos]

            pos = pos + 1

        # Works since one of them will have nothing to append
        res = res + word1[pos:]
        res = res + word2[pos:]


        return res

        # Same solution but with lists
        """
        while pos < len(word1) and pos < len(word2):
            res.append(word1[pos])
            res.append(word2[pos])

            pos = pos + 1

        # Works since one of them will have nothing to append
        res.append(word1[pos:])
        res.append(word2[pos:])


        return "".join(res)
        
        """