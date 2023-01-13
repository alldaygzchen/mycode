class Solution:
    def partitionLabels(self, s):
        res = []
        size = 0
        end = 0        
        lastIndexDic = {}
        
        for idx,c in enumerate(s):
            lastIndexDic[c] = idx
        
        for idx,c in enumerate(s):
            size+=1
            end = max(end,lastIndexDic[c])

            if idx ==end:
                res.append(size)
                size =0

        return res 

        