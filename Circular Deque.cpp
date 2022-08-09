class MyCircularDeque {
public:
    struct queue
    {
        int num;
        queue *next;
        queue *prev;
    };
    
    struct queue *front = NULL;
    struct queue *back = NULL;
    struct queue *temp = NULL;
    int size;
    int orignalSize;
    
    MyCircularDeque(int k) {
        size = k;
        orignalSize = k;
    }
    
    bool insertFront(int value) {
        if(isFull())
            return false;
        else
        {
            if(front == NULL)
            {
                queue *temp2 = new queue;
                temp2->num = value;
                temp2->next = NULL;
                temp2->prev = NULL;
                
                front = temp2;
                back = front;
                size--;
                return true;
            }
            else
            {
                queue *temp2 = new queue;
                temp2->num = value;
                temp2->next = front;
                front->prev = temp2;
                temp2->prev = NULL;
                front = temp2;
                
                size--;
                return true;
            }
        }
    }
    
    bool insertLast(int value) {
        if(isFull())
            return false;
        else
        {
            if(back == NULL)
            {
                queue *temp2 = new queue;
                temp2->num = value;
                temp2->next = NULL;
                temp2->prev = NULL;
                
                back = temp2;
                front = back;
                size --;
                return true;
            }
            else
            {
                queue *temp2 = new queue;
                temp2->num = value;
                back->next = temp2;
                temp2->next = NULL;
                temp2->prev = back;
                
                back = temp2;
                size--;
                return true;
            }
        }
    }
    
    bool deleteFront() {
        if(isEmpty())
            return false;
        else
        {
            if(orignalSize - size == 1)
            {
                temp = front;
                front = NULL;
                back = NULL;
                delete temp;
                 size++;
                return true;
            }
            else
            {
                temp = front;
                front = temp->next;
                front->prev = NULL;
                delete temp;
                size++;
                return true;
            }
        }
    }
    
    bool deleteLast() {
        if(isEmpty())
            return false;
        else
        {
            if(orignalSize - size == 1)
            {
                temp = back;
                back = NULL;
                front = NULL;
                delete temp;
                 size++;
                return true;
            }
            else
            {
                temp = back;
                back = temp->prev;
                back->next = NULL;
                delete temp;
                size++;
                return true;
            }
        }
    }
    
    int getFront() {
        if(isEmpty())
            return -1;
        else
            return front->num;
    }
    
    int getRear() {
        if(isEmpty())
            return -1;
        else
            return back->num;
    }
    
    bool isEmpty() {
        if(size == orignalSize)
            return true;
        else
            return false;
    }
    
    bool isFull() {
        if(size == 0)
            return true;
        else
            return false;
    }
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */
