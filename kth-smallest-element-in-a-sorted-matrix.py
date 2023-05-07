class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        def leftChild(i):
            return 2 * i + 1


        def rightChild(i):
            return 2 * i + 2

        def heapify_down(arr, n, current):
            left = leftChild(current)
            right = rightChild(current)

            if left < n and arr[left] < arr[current]:
                arr[current], arr[left] = arr[left], arr[current]
                heapify_down(arr, n, left)

            if right < n and arr[right] < arr[current]:
                arr[current], arr[right] = arr[right], arr[current]
                heapify_down(arr, n, right)

        heapify(matrix)

        for _ in range(k-1):
            heappop(matrix[0])
            heapify_down(matrix,len(matrix),0)
            if not len(matrix[0]):
                heappop(matrix)

        return matrix[0][0]