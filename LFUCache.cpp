class LFUCache {
public:
    struct ListNode {
        int val;
        int key;
        int freq;
        ListNode *next;
        ListNode *prev;
    };
    vector<vector<ListNode *>> v = {{NULL,NULL}};
    vector<ListNode *>r;
    int n;
    unordered_map<int,ListNode*>m;
    int position = 0;
    bool isZero = false;
    
    void InsertNode(int key, int value, int freq, ListNode *head, ListNode *tail)
    {
        if(head == NULL)
        {
            ListNode *temp = new ListNode;
            temp -> val = value;
            temp -> key = key;
            temp -> freq = freq;
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
            temp -> freq = freq;
            temp -> next = NULL;
            tail -> next = temp;
            temp -> prev = tail;
            tail = temp;
        }
        r[0] = head;
        r[1] = tail;
        m[key] = tail;
    }
    
    void DeleteNode(ListNode *temp, ListNode *head, ListNode *tail, int key)
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
                if(v[position][0] == head)
                    position++;
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
        r[0] = head;
        r[1] = tail;

        delete temp;
        m.erase(key);
    }
    
    /////////////////////////////////////////////////////
    
    LFUCache(int capacity) {
        n = capacity;
        if(capacity == 0)
            isZero = true;
        r.push_back(NULL);
        r.push_back(NULL);
    }
    
    int get(int key) {
        if(m.find(key) == m.end())
            return -1;
        else
        {
            int freq = m[key]->freq+1;
            int value = m[key]->val;
            
            DeleteNode(m[key],v[freq - 1][0],v[freq - 1][1],key);
            v[freq - 1][0] = r[0];
            v[freq - 1][1] = r[1];
            int k = v.size();
            if(k > freq)
            {
                InsertNode(key,value,freq,v[freq][0],v[freq][1]);
                v[freq][0] = r[0];
                v[freq][1] = r[1];
            }
            else
            {
                ListNode *head = NULL;
                ListNode *tail = NULL;
                vector<ListNode *>a = {head,tail};
                v.push_back(a);
                InsertNode(key,value,freq,v[freq][0],v[freq][1]);
                v[freq][0] = r[0];
                v[freq][1] = r[1];
            }
            
            return m[key]->val;
        }
    }
    
    void put(int key, int value) {
        if(isZero)
            return;
        if(n > 0)
        {
            if(m.find(key) == m.end())
            {
                InsertNode(key,value,0,v[0][0],v[0][1]);
                v[0][0] = r[0];
                v[0][1] = r[1];
                position =  0;
                n--;
            }
            else
            {
                int freq = m[key]->freq + 1;
                DeleteNode(m[key],v[freq - 1][0],v[freq - 1][1],key);
                v[freq - 1][0] = r[0];
                v[freq - 1][1] = r[1];
                int k = v.size();
                if(k > freq)
                {
                    InsertNode(key,value,freq,v[freq][0],v[freq][1]);
                    v[freq][0] = r[0];
                    v[freq][1] = r[1];
                }
                else
                {
                    ListNode *head = NULL;
                    ListNode *tail = NULL;
                    vector<ListNode *>a = {head,tail};
                    v.push_back(a);
                    InsertNode(key,value,freq,v[freq][0],v[freq][1]);
                    v[freq][0] = r[0];
                    v[freq][1] = r[1];
                }
            }
        }
        else
        {
            if(m.find(key) == m.end())
            {
                DeleteNode(v[position][0],v[position][0],v[position][1],v[position][0]->key);
                if(r[0] == NULL)
                {
                    v[position-1][0] = r[0];
                    v[position-1][1] = r[1];
                }
                else
                {
                    v[position][0] = r[0];
                    v[position][1] = r[1];
                }
                InsertNode(key,value,0,v[0][0],v[0][1]);
                v[0][0] = r[0];
                v[0][1] = r[1];
                position = 0;
            }
            else
            {
                int freq = m[key]->freq + 1;
                DeleteNode(m[key],v[freq - 1][0],v[freq - 1][1],key);
                v[freq - 1][0] = r[0];
                v[freq - 1][1] = r[1];
                int k = v.size();
                if(k > freq)
                {
                    InsertNode(key,value,freq,v[freq][0],v[freq][1]);
                    v[freq][0] = r[0];
                    v[freq][1] = r[1];
                }
                else
                {
                    ListNode *head = NULL;
                    ListNode *tail = NULL;
                    vector<ListNode *>a = {head,tail};
                    v.push_back(a);
                    InsertNode(key,value,freq,v[freq][0],v[freq][1]);
                    v[freq][0] = r[0];
                    v[freq][1] = r[1];
                }
            }
        
        }
    }
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
