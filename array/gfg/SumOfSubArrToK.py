class Solution:
    def subArraySum(self,arr, n, s): 
        #Write your code here
        sum = 0
        track=[]
        last=0
        count =0
        start=0
        for i in range(0,n):
            if sum < s:
                track.append(arr[i])
                last= last +1
                sum = sum + arr[i]
            elif sum > s:
                start=start+1
                pop=track.pop(0)
                sum=sum-pop
            else:
                count = count +1
        return count


if __name__=='__main__':
    solution=Solution()
    arr=[2,3,5,7,1,3,8,10]
    arr=[1,1,1]
    #arr =[1]
    n=3
    s=2
    print(solution.subArraySum(arr,n,s))