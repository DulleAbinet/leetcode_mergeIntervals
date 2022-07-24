class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])
        new_arr = [intervals[0]]
        for firIdx,endIdx in intervals[1:]:
            lastInd = new_arr[-1][1]
            if firIdx <= lastInd :
                new_arr[-1][1] = max(lastInd,endIdx)
            else:
                new_arr.append([firIdx,endIdx])
        
        return new_arr                
