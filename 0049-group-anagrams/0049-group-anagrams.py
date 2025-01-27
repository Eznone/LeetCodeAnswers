class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        ans_dict = {}

        for string in strs:
            cur_str = ''.join(sorted(string))
            
            if cur_str not in ans_dict:
                ans_dict[cur_str] = [string]
            else:
                ans_dict[cur_str].append(string)

        return ans_dict.values()
