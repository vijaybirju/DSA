class Solution:	
    #Function to reverse every sub-array group of size k.
	def reverseInGroups(self, arr, N, K):
		# code here
		reverse_arr =[]
		for i in range(0,(N-1)//K):
                    divide = i*K
                    new_arr = arr[:divide]
                    new_arr=sorted(new_arr,reverse=True)
                    reverse_arr=reverse_arr+new_arr
        return
		    
		    
