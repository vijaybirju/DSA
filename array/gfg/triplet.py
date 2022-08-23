
class Solution:
    #Function to find triplets with zero sum.    
    def findTriplets(self, arr, n):
        
        arr=sorted(arr)
        for i in range(0,len(arr)-2):
            start=i+1
            end=n-1
            while (start<end) :
                print("i ",arr[i])
                print("start ",arr[start])
                print('end ',arr[end])
                
                if (arr[i]+arr[start]+arr[end])==0:
                    return 1
                elif (arr[i]+arr[start]+arr[end]) < 0:
                    start += 1
                else:
                    end -= 1
        return False
                


test={
    'input':{
        'arr':[0, -1, 2, -3, 1],
        'n':5
    },
    'output':1
}

tests=[test]
tests.append(
    {
        'input':{
            'arr':[],
            'n':0
        },
        'output':0
    }
)



if __name__=='__main__':
    solution=Solution()
    print('test 1',solution.findTriplets(tests[0]['input']['arr'],tests[0]['input']['n']))
    print('test 2',solution.findTriplets(tests[1]['input']['arr'],tests[1]['input']['n']))