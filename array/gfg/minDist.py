
# Write Python 3 code in this online editor and run it.


class Solution:
    def minDist(self, arr, n, x, y):
        idx1=-1
        idx2=-1
        min_dist=n
        for i in range(0,n):
            if arr[i]==x:
                idx1=i
            elif arr[i]==y:
                idx2=i
            if idx1!=-1 and idx2!=-1:
                min_dist=min(min_dist,abs(idx1-idx2))
                
        if idx1==-1 or idx2==-1:
            return -1
        else:
            return min_dist
        
#arrs = [{
#    'arr':[ 3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3]
#    
#}]
#
#arrs.append(arr)
#a
if __name__ == "__main__" :
    solution=Solution() 
    arr = [ 3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3]
    arr=[1,2]
    n = len(arr)
    x = 1
    y = 2
    print ("Minimum distance between %d and %d is %d\n"%( x, y,solution.minDist(arr, n, x, y)));

            
        
