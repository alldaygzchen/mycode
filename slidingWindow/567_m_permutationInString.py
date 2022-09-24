
# trick 
# return s1_map ==s2_map

class Solution:

    def getAndAdd(self,string,dict_map):
        if string in dict_map:
            dict_map[string]+=1
        else:
            dict_map[string]=1

    def getAndMinus(self,string,dict_map):

        dict_map[string]-=1
        
        if dict_map[string]==0:
            dict_map.pop(string)


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

        if s1_map ==s2_map:
                return True


        while r < len(s2):

            if s1_map ==s2_map:
                return True



            self.getAndAdd(s2[r],s2_map)
            self.getAndMinus(s2[l],s2_map)

            # if s1_map ==s2_map:
            #     return True

            l+=1
            r+=1

        return s1_map ==s2_map
            
            

s =Solution()
print(s.checkInclusion("adc","dcda"))

