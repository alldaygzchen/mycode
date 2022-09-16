class Solution:
    def isAnagram(self, s, t):
        
        res = False
        map_s= {} #ele=>count
        map_t = {}
        
        for e in s:
            if e not in map_s:
                map_s[e]= 1
            else:
                map_s[e]+=1
                
        for e in t:
            if e not in map_t:
                map_t[e]= 1
            else:
                map_t[e]+=1
                
        if map_t == map_s:
            res = True
        
    
        
        
        return res
        