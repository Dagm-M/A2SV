class MyLinkedList {
public:
    struct ListNode {
        int val;
        ListNode *next;
  };
    
    ListNode *head;
    ListNode *tail;
    ListNode *temp;
    MyLinkedList() {
        head = NULL;
        tail = head;
    }
    
    int get(int index) {
        temp = head;
        for(int i = 0 ; i < index ; i++)
        {
            if(temp == NULL)
                return -1;
            temp = temp->next;
        }
        if(temp != NULL)
            return temp->val;
        return -1;
    }
    
    void addAtHead(int val) {
        ListNode *temp2 = new ListNode;
        temp2->val = val;
        temp2->next = head;
        if(tail == NULL)
            tail = temp2;
        head = temp2;

    }
    
    void addAtTail(int val) {
        ListNode *temp2 = new ListNode;
        temp2->val = val;
        temp2->next = NULL;
        if(tail != NULL)
            tail->next = temp2;
        if(head == NULL)
            head = temp2;
        tail = temp2;
    }
    
    void addAtIndex(int index, int val) {
        temp = head;
        ListNode *temp2 = new ListNode;
        temp2->val = val;
        ListNode *temp1 = head;
        if(index == 0)
        {
            temp2->next = temp;
            head = temp2;
            return;
        }
        for(int i = 0 ; i<index; i++)
        {
            temp1 = temp;
            if(temp != NULL)
            {
                temp = temp->next;
            }
            
            if(temp1 == NULL)
                return;
        }
        temp1->next = temp2;
        temp2->next = temp;
        if(temp == NULL)
            tail = temp2;
    }
    
    void deleteAtIndex(int index) {
        temp = head;
        ListNode *temp1 = head;
        if(index == 0)
        {
            head = temp->next;
            delete temp;
            return;
        }
        for(int i = 0 ; i<index; i++)
        {
            temp1 = temp;
            temp = temp->next;
            if(temp == NULL)
                return;
        }
        temp1->next = temp->next;
        if(temp == tail)
            tail = temp1;
        delete temp;
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */
