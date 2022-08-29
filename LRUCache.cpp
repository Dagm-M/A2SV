class LRUCache {
public:
    struct ListNode {
        int val;
        int key;
        ListNode *next;
        ListNode *prev;
    };
    
    ListNode *head = NULL;
    ListNode *tail = NULL;
    int n;
    unordered_map<int,ListNode*>m;
    
    void toFront(ListNode* temp)
    {
        if(head == tail)
            return;
        if(temp == head)
        {
            head = head->next;
            head->prev = NULL;
            temp -> next = NULL;
            tail -> next = temp;
            temp -> prev = tail;
            tail = temp; 
        }
        else if(temp == tail)
            return;
        else
        {
            temp -> prev -> next = temp -> next;
            temp -> next -> prev = temp -> prev;
            temp -> next = NULL;
            tail -> next = temp;
            temp -> prev = tail;
            tail = temp; 
        }
    }
    
    void InsertNode(int key, int value)
    {
        if(head == NULL)
        {
            ListNode *temp = new ListNode;
            temp -> val = value;
            temp -> key = key;
            temp -> next = NULL;
            temp -> prev = NULL;
            head = temp;
            tail = head;
        }
        else
        {
            ListNode *temp = new ListNode;
            temp -> val = value;
            temp -> key = key;
            temp -> next = NULL;
            tail -> next = temp;
            temp -> prev = tail;
            tail = temp;
        }
        m[key] = tail;
    }
    
    void DeleteNode(ListNode *temp,int key)
    {
        if(temp == head)
        {
            if(head->next != NULL)
            {
                head = head->next;
                head->prev = NULL;
            }
            else
            {
                head = NULL;
                tail = NULL;
            }
            
        }
        else if(temp == tail)
        {
            temp -> prev -> next = NULL;
            tail = temp -> prev;
        }
        else
        {
            temp -> prev -> next = temp ->next;
            temp -> next -> prev = temp ->prev;
        }

        delete temp;
        m.erase(key);
    }
    ///////////////////////////////////////////////////////////////////////////
    
    LRUCache(int capacity) {
        n = capacity;
    }
    
    int get(int key) {
        if(m.find(key) == m.end())
            return -1;
        else
        {
            ListNode *temp = m[key];
            toFront(temp);
            return temp->val;
        }
    }
    
    void put(int key, int value) {
        if(n > 0)
        {
            if(m.find(key) == m.end())
            {
                InsertNode(key,value);
                n--;
            }
            else
            {
                ListNode* temp = m[key];
                DeleteNode(temp,temp->key);
                InsertNode(key,value);
            }
        }
        else
        {
            if(m.find(key) == m.end())
            {
                DeleteNode(head,head->key);
                InsertNode(key,value);
            }
            else
            {
                ListNode *temp = m[key];
                DeleteNode(temp,temp->key);
                InsertNode(key,value);
            }
        
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
