class Solution:
    def topKFrequent(self, nums, k):
        res = []
        freq_map = {} #ele => count
        freq_list = [[] for i in range(len(nums) + 1)] #count

        for num in nums:
            if num in freq_map:
                freq_map[num]+=1
            else:
                freq_map[num]=1

        for key,val in freq_map.items():
            freq_list[val].append(key)


        for idx in range(len(freq_list)-1,-1,-1):
            for n in freq_list[idx]:
                res.append(n)
                if len(res) == k:
                    return res

s = Solution()
print(s.topKFrequent([1,1,1,2,2,3],2))