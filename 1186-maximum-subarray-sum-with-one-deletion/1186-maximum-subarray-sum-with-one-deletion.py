class Solution(object):
    def maximumSum(self, arr):
        i=0
        result=arr[i]
        nodelete=arr[i]
        onedelete = float('-inf')
        for i in range(1,len(arr)):
            prevnodelete=nodelete
            prevonedelete=onedelete
            nodelete=max((nodelete+arr[i]),arr[i])
            if prevonedelete==float('-inf'):
                onedelete=prevnodelete
            else:
                v=prevonedelete+arr[i]
                onedelete=max(v,prevnodelete)

            result=max(result,onedelete,nodelete)
        return result

        