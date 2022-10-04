class Solution:
    def largestRectangleArea(self, heights):

        result = float('-inf')
        stackForRight = [] #include area from index to end

        for idx,h in enumerate(heights):

            restore_idx = idx
            while stackForRight and stackForRight[-1][1]>h: #include idex area and area below the index
                last_idx,last_h = stackForRight.pop()
                result = max(result,last_h*(idx-last_idx))
                restore_idx = last_idx
            stackForRight.append((restore_idx,h))



        for i,h in stackForRight:
            result = max(result,h*(len(heights)-i))

        return result