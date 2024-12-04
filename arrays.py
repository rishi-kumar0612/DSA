def alter (arr, N):

    if N == 0 :
        return -1
    else:
        for idx in range (N):
            if (idx%2 == 0):
                print(arr[idx], end = ",")
        

def searchy(arr,m):
    if type(m) == "int":

        for i in range(0,len(arr)):
            if arr[i] == m:
                print("Item found %d",m)
                return m
    
         

if __name__ == "__main__" :

    arr = [1,2,3,4,5,6,7,8,9]
    N = len(arr)
    m = 4
    searchy(arr,m)

