from collections import defaultdict

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        dict_x = defaultdict(list)
        dict_y = defaultdict(list)
        dict_box = defaultdict(list)
        
        for y, row in enumerate(board):
            for x, num in enumerate(row):

                if num == '.':
                    continue

                if num in dict_x[x] or num in dict_y[y] or num in dict_box[(x//3, y//3)]:
                    return False

                dict_x[x].append(num)
                dict_y[y].append(num)
                dict_box[(x//3, y//3)].append(num)

        return True


                