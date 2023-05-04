class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify_down(arr,n,i)
            
    def leftChild(self,i):
        return 2 * i + 1


    def rightChild(self,i):
        return 2 * i + 2
    
    #Function to build a Heap from array.
    def heapify_down(self,arr, n, current):
        left = self.leftChild(current)
        right = self.rightChild(current)
        smallest = current
    
        if left < n and arr[left] > arr[smallest]:
            smallest = left
    
        if right < n and arr[right] > arr[smallest]:
            smallest = right
            
        if current != smallest:
            arr[current], arr[smallest] = arr[smallest], arr[current]
            self.heapify_down(arr, n, smallest)

    def HeapSort(self, arr, n):
        self.heapify(arr)
        
        for i in range(n-1,0,-1):
            arr[0], arr[i] = arr[i],arr[0]
            self.heapify_down(arr,i,0)
        
        return arr
