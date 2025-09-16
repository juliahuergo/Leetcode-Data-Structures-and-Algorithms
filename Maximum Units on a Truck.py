class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        ans = 0 #total number of units
        totalBoxes = 0
        
        boxTypes.sort(key =lambda x: x[1], reverse=True)
        i = 0
        
        while totalBoxes < truckSize and i < len(boxTypes):
            round = min(boxTypes[i][0], truckSize - totalBoxes)
            totalBoxes += round
            ans += round * boxTypes[i][1]
            
            i+=1
        
        return ans
