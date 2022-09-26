class Solution:

    def getAndAdd(self,string,dict_map):

        dict_map[string]= dict_map.get(string,0)+1


    def getAndMinus(self,string,dict_map):

        dict_map[string]-=1
        
        # if dict_map[string]==0:
        #     dict_map.pop(string)


    def checkInclusion(self, s1, s2):
        
        res =False
        l=0
        r= len(s1)
        s1_map = dict()
        s2_map = dict()

        if len(s1) > len(s2):
            return False

        for idx in range(len(s1)):

            self.getAndAdd(s1[idx],s1_map)
            self.getAndAdd(s2[idx],s2_map)

        

        s1_cond = len(s1_map)
        s2_cond = 0

        for e in s1_map:
            if e in s2_map and s1_map[e] == s2_map[e]:
                s2_cond+=1



        if s1_cond ==s2_cond:
            return True


        while r < len(s2):

            self.getAndAdd(s2[r],s2_map)
            
            if s2[r] in s1_map and s2_map[s2[r]]==s1_map[s2[r]]:
                s2_cond +=1
            elif s2[r] in s1_map and s2_map[s2[r]]-1==s1_map[s2[r]]:
                s2_cond -=1
            

            self.getAndMinus(s2[l],s2_map)
            
            if s2[l] in s1_map and s2_map[s2[l]]==s1_map[s2[l]]:
                s2_cond +=1
            elif s2[l] in s1_map and s2_map[s2[l]]+1==s1_map[s2[l]]:
                s2_cond -=1

            

            if s1_cond ==s2_cond:
                return True

            l+=1
            r+=1

        return res      