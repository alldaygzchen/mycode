#consider value as pointer

class Solution:
    def findDuplicate(self, nums) -> int:

        slow, fast = 0,0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        start = 0

        while True:


            slow = nums[slow]
            start = nums[start]

            if slow == start:
                return start 
        