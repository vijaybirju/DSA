
def rotate( arr, n):
    new_arr = []
    print(arr[n-1:])
    new_arr= arr[n-1:]+arr[:-1]
    arr=new_arr
    return arr
    

arr=[1, 2, 3, 4, 5]

if __name__=='__main__':
    print(rotate(arr,5))