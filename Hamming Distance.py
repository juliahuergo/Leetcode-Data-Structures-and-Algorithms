class Solution(object):
    def hammingDistance(self, x, y):
        count = 0
        z = x^y 
        while z > 0:
            if z & 1 == 1: #last bit is 1
                count += 1
            z >>= 1 #shift right once
        return count
