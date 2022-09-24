class Solution:
    def minWindow(self, teststring, substring):
        
        substring_map = dict()
        window_map = dict()
        
        for e in substring:
            substring_map[e] = substring_map.get(e,0)+1

        window_cond,substring_cond =0,len(substring_map)


        l=0
        r=0
        resLen = float("infinity")

        # window_map[teststring[r]] = 1+ window_map.get(teststring[r],0)
        # if teststring[r] in substring_map and window_map[teststring[r]] == substring_map[teststring[r]]:
        #     window_cond+=1

        while r<len(teststring):
            
            print('l',l,'r',r)
            print('window_map',window_map,'substring_map',substring_map)
            print('window_cond',window_cond,'substring_cond',substring_cond)
            
            while window_cond == substring_cond:
                # print('##########################')
                # print(window_cond,window_cond)
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # print('###',teststring[l],window_map)
                # print(resLen)
                window_map[teststring[l]]-=1
                if teststring[r] in substring_map and window_map[teststring[l]] < substring_map[teststring[l]]:
                    window_cond -=1
                l+=1


            window_map[teststring[r]] = 1+ window_map.get(teststring[r],0)
            if teststring[r] in substring_map and window_map[teststring[r]] == substring_map[teststring[r]]:
                window_cond+=1
            r+=1

        ######################################################

        if window_cond == substring_cond:
            if (r - l + 1) < resLen:
                res = [l, r]
                resLen = r - l + 1
                
            window_cond[teststring[l]]-=1
            if window_map[teststring[l]] < substring_map[teststring[l]]:
                window_cond -=1
            l+=1

        l, r = res
        return teststring[l : r + 1] if resLen != float("infinity") else ""

s= Solution()
s.minWindow("ADOBECODEBANC","ABC")


   