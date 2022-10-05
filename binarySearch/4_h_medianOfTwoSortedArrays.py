#A = [0,...i,i+1..len(A)-1]
#B = [0,...j,j+1..len(B)-1]
#len([0,..,i,0,...,j])=(len(A)+len(B))//2
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        res = None
        
        if len(nums1)<=len(nums2):
            A,B=nums1,nums2
        else:
            B,A=nums1,nums2

        half = (len(A)+len(B))//2 #Not including left partition

        l,r = 0,len(A)-1

        while True:
            #print('#l,r',l,r)

            i = (l+r)//2
            j = half-i-1-1
            
            #print('#i,j',i,j)

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
            
            #print(Aleft,Aright,Bleft,Bright)


            if Aleft<=Bright and Bleft<=Aright:

                if (len(A)+len(B))%2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft>Bright:
                r=i-1
            else:
                l=i+1
                
            #print('##l,r',l,r)
            
        return res

        