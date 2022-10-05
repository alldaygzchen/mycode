

class TimeMap:

    def __init__(self):
        self.store = {} #key:[[val1,time1],[val2,time2]]
        

    def set(self, key, value, timestamp):

        if key in self.store:
            self.store[key].append([value,timestamp])
        else:
            self.store[key] = [[value,timestamp]]
        

    def get(self, key, timestamp):

        values =self.store.get(key,[])
        res = ""
        
        l,r=0,len(values)-1
        
        while l<=r:
            m = (l+r)//2

            if values[m][1]<=timestamp:
                res = values[m][0]
                l =m+1
            else:
                r = m-1
        
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)