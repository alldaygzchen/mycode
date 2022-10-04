from operator import truediv


class Solution:
    def searchMatrix(self, matrix, target):

        top,bot = 0,len(matrix)-1
        l,r = 0,len(matrix[0])-1

        while top<=bot: #maybe no return
            mid_row = (top+bot)//2

            if target >matrix[mid_row][-1]:
                top = mid_row +1
            elif target < matrix[mid_row][0]:
                bot = mid_row -1 
            else:
                break

        if top>bot:
            return False
        
        while l<=r:
            mid_col=(l+r)//2

            if target>matrix[mid_row][mid_col]:
                l = mid_col+1
            elif target<matrix[mid_row][mid_col]:
                r = mid_col-1
            else:
                res = True
                return res
        return False







        return 