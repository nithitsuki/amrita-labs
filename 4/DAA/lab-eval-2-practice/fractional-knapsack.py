# https://leetcode.com/problems/maximum-units-on-a-truck/
from ast import List
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=(lambda x: x[1]), reverse=True)
        units: int = 0
        for box in boxTypes:
            no_boxes: int = box[0]
            if(no_boxes <= truckSize):
                units = units + (no_boxes*box[1])
                truckSize = truckSize - no_boxes
            elif(no_boxes > truckSize):
                units = units + (truckSize*box[1])
                truckSize = truckSize - truckSize
        return units