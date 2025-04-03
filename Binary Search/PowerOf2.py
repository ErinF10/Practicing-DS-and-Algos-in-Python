# https://leetcode.com/problems/power-of-two/

 # M: binary search, similar to finding the sqrt of a num
  # P: We can start in the middle and work our way to the solutions
  #
  #   is 16 a power of 2?
  #   take 2^8 > 16
  #   take 2^3 < 16
  #   take 2^6 > 16
  #   take 2^5 == 16
  #    0  1  2  3  4   5   6   7    8 
  #    1  2  4  8  16  32  64  128  256
  #                SL   M     

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
          
        smaller = 0
        larger = 31
        while smaller <= larger:
            mid = smaller + (larger - smaller)//2
            if 2 ** mid < n:
                smaller = mid + 1
            elif 2 ** mid > n:
                larger = mid - 1
            else:
                return True
        return False

