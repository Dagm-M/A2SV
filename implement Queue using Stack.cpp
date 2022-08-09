class MyQueue {
public:
    vector<int> stack;
    MyQueue() {
    }
    
    void push(int x) {
        stack.push_back(x);
    }
    
    int pop() {
        int a = stack[0];
        stack.erase(stack.begin());
        return a;
    }
    
    int peek() {
        return stack[0];
    }
    
    bool empty() {
        return stack.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
