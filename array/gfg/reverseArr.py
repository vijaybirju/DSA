class Solution:
    def reverseInGroups(self, arr, N, K):
        reverse_arr=[]
        for i in range(0,(N)//3):
            divide = (i+1)*K
            temp_arr=arr[:divide]
            temp_arr=sorted(temp_arr,reverse=True)
            reverse_arr=reverse_arr+temp_arr
        temp_2=arr[(K*((N)//3)):]
        temp_2=sorted(temp_2,reverse=True)
        reverse_arr=reverse_arr+temp_2
        return reverse_arr

test={
    'input':{
        "arr":[1,2,3,4,5],
        'N':5,'K':3
        
    },
    'output':[3,2,1,5,4]
    
}
tests=[test]

tests.append(
    {
        "input":
    {
        "arr":[1,2],
    "N":2,"K":3
    },
    'output':[2,1]
})





if __name__=='__main__':
    solution=Solution()
    print( solution.reverseInGroups( tests[0]['input']['arr'], tests[0]['input']['N'], tests[0]['input']['K'] ))