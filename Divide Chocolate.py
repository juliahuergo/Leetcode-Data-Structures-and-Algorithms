class Solution(object):
    def maximizeSweetness(self, sweetness, k):
       
        def check(x): 
            total = 0
            i = 0
            while i < len(sweetness):
                sw = 0
                while sw < x and i < len(sweetness):
                    sw += sweetness[i]
                    i += 1
                if sw >= x:
                    total += 1
            
            return total >= (k+1)

        left = min(sweetness)
        right = sum(sweetness) // (k+1) #max when all chunks are as sweet
        
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right
