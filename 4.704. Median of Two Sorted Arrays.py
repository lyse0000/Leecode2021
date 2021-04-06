# 704. Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        L, R = 0, len(nums)-1
        
        while L<= R:
            mid = (R-L)//2+L
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                L = mid+1
            else:
                R = mid-1
                
        return -1
        
# ========================================================================================================        
# 4. Median of Two Sorted Arrays
class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        """
         0 1 2 3 4 5                    0 1 2 3 4 5 6 7
        [1 3 5 7 9 11]     len = 6     [1 2 3 4 5 8 10 12]     len = 8
        
        k = (8+6)//2 -1 = 6. 7
        m1, m2 = 3, 4    3+4 = 7> K
            每次砍掉1/4 m1 or m2 的 前或后
            if k>sum:
                砍小的的前面 然后k要缩小小的前面的那部分的1/2
            
            if K<=sum
                m1跟m2 谁大砍谁后面
                
        K = 6
         0 1 2 3 4 5                   0 1 2 3 4 5 6  7
        [1 3 5 7 9 11]     m1 = 3     [1 2 3 4 5 8 10 12]     m2 = 4
                
        K = 6
         0 1 2 3                       0 1 2 3 4 5 6  7
        [1 3 5 7]     m1 = 2          [1 2 3 4 5 8 10 12]     m2 = 4
        
        K = 6
         0 1                           0 1 2 3 4 5 6  7
        [1 3]     m1 = 1              [1 2 3 4 5 8 10 12]     m2 = 4
         
        K = 6 砍前面 谁小砍谁 update k。 New K = 6-2 【2 = len of 被砍掉的】
         0                             0 1 2 3 4 5 6  7
        [5]     m1 = 0                [1 2 3 4 5 8 10 12]     m2 = 4
        
        K = 4 都一样 
         0                             0 1 2 3 4 5 6  7
        [5]     m1 = 0                [1 2 3 4 5 8 10 12]     m2 = 4
        
        
        [1,1,2]  4
        [1,1,1,2] 这就是为啥可以砍掉[i] 因为两个0开始他们是多的
        
        """
        
        L = len(A)+len(B)
        if L%2: 
            return self.findKth(A, B, L//2)
        else:
            return float(self.findKth(A, B, L//2-1) + self.findKth(A, B, L//2))/2
        
        
        
    def findKth(self, A, B, k):
        if not A:
            return B[k]
        if not B:
            return A[k]
        
        a, b = len(A)//2, len(B)//2
        midA, midB = A[a], B[b]
        
        if k > a+b:         # k在后面， 砍前面小的
            if midA < midB:
                return self.findKth(A[a+1:], B, k-a-1)
            else:
                return self.findKth(A, B[b+1:], k-b-1)
        else:               # k在前面， 看后面大的
            if midA > midB:
                return self.findKth(A[:a], B, k)
            else:
                return self.findKth(A, B[:b], k)
        
