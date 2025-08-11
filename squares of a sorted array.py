class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = []
        i = j = 0            #i for nums and j for squares
        
        while i < len(nums):
            square = nums[i] * nums[i]
            
            if j != 0:
                temp = j
                while(square < squares[temp-1] and temp > 0):
                    temp -= 1
                squares.insert(temp, square)
            
            else: 
                squares.append(square)
                
            i += 1
            j += 1
            
        return squares
