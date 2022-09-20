class Solution:
    
    def groupAnagrams(self, strs):
        
        res = []
        str_map = {} #sort=>list()

        for str in strs:
            sorted_word = ('').join(sorted(str))
            print('sorted_word',sorted_word)
            if sorted_word in str_map:
                str_map[sorted_word].append(str)
            else:
                str_map[sorted_word] = [str]

        print('str_map',str_map)

        for ele in str_map.values():
            if ele != []:
                res.append(ele)

        return res


s = Solution()
print(s.groupAnagrams(['eat', 'ate', 'tea', 'ant', 'tan','bat', 'adobe', 'abode', 'listen', 'silent']))
print(s.groupAnagrams([""]))








