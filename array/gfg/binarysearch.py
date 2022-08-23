class Solution:
    #Complete the below function
    def search(self,arr, N, X):
        #Your code here
        lo,hi=0,N-1
        sort_arr = sorted(arr)
        while lo<=hi:
            mid = (lo+hi)//2
            if sort_arr[mid]==X:
                if sort_arr[mid-1]==X:
                    hi = mid-1
                else:
                    return mid
            elif sort_arr[mid]<X:
                lo=mid+1
            else:
                hi = mid-1
        return -1
                

if __name__=='__main__':
    arr=[1,2,3,4,4,7,7,7,7,8,9,10,11,12]
    N=14
    X=7
    solution=Solution()
    print(solution.search(arr,N,X))