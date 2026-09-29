class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        start1=intervals[0][0]
        end1=intervals[0][1]
        result=[]
        for i in range(1,len(intervals)):
            start2=intervals[i][0]
            end2=intervals[i][1]

            if end1>=start2:
                start1=start1
                end1=max(end1,end2)
                continue
            else:
                result.append([start1, end1])
                start1=start2
                end1=end2

        result.append([start1, end1])

        return result
            
            

        
        