# Enter your code here. Read input from STDIN. Print output to STDOUT
numOfWords = int(input())
A = {}
for i in range(numOfWords):
    word = input()
    if(word in A):
        A[word] = A[word] + 1
    else:
        A[word] = 1
    
    
    
print(len(A))
for value in A.values():
    print(value, end= " ")

