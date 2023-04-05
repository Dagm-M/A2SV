class Solution: 
    def select(self, arr, i):
        pass
    
    def selectionSort(self, arr,n):
        for i in range(n):
            s = i
            for j in range(i,n):
                if arr[s] > arr[j]:
                    s = j
                
            arr[i],arr[s] = arr[s], arr[i]
            
        return arr
