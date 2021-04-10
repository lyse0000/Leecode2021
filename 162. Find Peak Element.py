class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        """
        # https://leetcode.com/problems/find-peak-element/discuss/50232/Find-the-maximum-by-binary-search-(recursion-and-iteration)  ->discussion
        
        The reason that Binary Search works here:

        -∞ __ ___ ___ ___ ___ -∞

        -∞ 1 2 __ ___ ___ 2 1 -∞ (This makes sure that the corner element is not the answer)

        -∞ 1 2 3 4 ___ 4 3 2 1 -∞ (Just trying to put answer away from corner)

        -∞ 1 2 3 4 5 4 3 2 1 -∞ (But at one time i will have to put a number which is the peak since) SINCE NO ADJACENT SAME ALLOWED

        Now lets try solving this


        | 1 | 2 | 3 | 4 | 5 | 4 | 3 | 2 | 1 |
        |---|---|---|---|---|---|---|---|---|
        | l | _ | _ | _ | m | _ | _ | _ | r |
        a[m] > a[m+1] -> r=m (Not m-1 since m is larger and it itself can be the answer)
        | 1 | 2 | 3 | 4 | 5 | 4 | 3 | 2 | 1 |
        |---|---|---|---|---|---|---|---|---|
        | l | m | _ | _ | r | X | X | X | X |

        a[m] < a[m+1] -> l = m+1 (Since m is smaller than m+1, m will for sure be not the answer)
        | 1 | 2 | 3 | 4 | 5 | 4 | 3 | 2 | 1 |
        |---|---|---|---|---|---|---|---|---|
        | X | X | l | m | r | X | X | X | X |

        a[m] < a[m+1] -> l = m+1 (Since m is smaller than m+1, m will for sure be not the answer)
        | 1 | 2 | 3 | 4 | 5   | 4 | 3 | 2 | 1 |
        |---|---|---|---|-----|---|---|---|---|
        | X | X | X | X | l,r | X | X | X | X |

        l is the answer
        
        """
        lo, hi = 0, len(nums)-1
        
        while lo<hi:
            mid = (lo+hi)//2
            mid2 = mid+1
            if nums[mid] > nums[mid2]:
                hi = mid
            else:
                lo = mid2
                
        return lo
