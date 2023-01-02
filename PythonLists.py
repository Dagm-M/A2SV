if __name__ == '__main__':
    N = int(input())
    myList = []
    for index in range(N):
        temp = input().split()
        if len(temp) == 3:
            myList.insert(int(temp[1]),int(temp[2]))
        elif len(temp) == 2:
            if temp[0] == "remove":
                myList.remove(int(temp[1]))
            elif temp[0] == "append":
                myList.append(int(temp[1]))
            
        else:
            if temp[0] == "print":
                print(myList)
            elif temp[0] == "sort":
                myList.sort()
            elif temp[0] == "pop":
                myList.pop()
            else:
                myList.reverse()
