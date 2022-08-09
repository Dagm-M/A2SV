class MinStack {
public:
    vector<int> *stack;
    vector<int> min;
    MinStack() {
        stack = new vector<int>;
    }
    
    void push(int val) {
        stack->push_back(val);
        min.push_back(val);
    }
    
    void pop() {
        stack->pop_back();
        min.pop_back();
    }
    
    int top() {
        if(stack->size() != NULL){
        int n = stack->size();
        return stack[0][n-1];}
        else
            return NULL;
    }
    
    int getMin() {
        int n = min.size();
        int m = min[0];
        for(int i = 1 ; i<n ; i++)
        {
            if(m > min[i])
                m = min[i];
        }
        return m;
    }
};


