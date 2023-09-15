#balanced-brackets------------------

def isBalanced(arr):
    stk = []
    for i in range (0,len(arr)) :
        if arr[i] == '(' or arr[i] == '[' or arr[i] == '{' :
            stk.append(arr[i])
            peek = stk[-1]
        elif arr[i] == ')' :
            if stk == [] :
                return 'NO'
            
            elif peek == '(' :
                stk.pop()
                if stk == [] :
                    pass
                else :
                    peek = stk[-1]
            else :
                return 'NO'
        elif arr[i] == ']' :
            if stk == [] :
                return 'NO'
            elif peek == '[' :
                stk.pop()
                if stk == [] :
                    pass
                else :
                    peek = stk[-1]
                
            else :
                return 'NO' 
                
        elif arr[i] =='}' :
            if stk == [] :
                return 'NO'
            elif peek == '{' :
                stk.pop()
                if stk == [] :
                    pass
                else :
                    peek = stk[-1]
            else :
                return 'NO'
                
    if stk == [] :
        return 'YES'
    else :
        return 'NO'
    

#game of two stacks--------------------------

def twoStacks(maxSum, a, b):
    arr = []
    st1_count = 0
    st2_count = 0
    totalsum = 0
    for i in range(0,len(a)) :
        if (totalsum + a[i]) > maxSum :
            break;
        totalsum = totalsum + a[i]
        st1_count = st1_count + 1
    arr.append(st1_count)
    
    for i in range(0,len(b)) :
        totalsum = totalsum + b[i]
        st2_count = st2_count + 1
        while totalsum > maxSum and st1_count > 0 :
            totalsum = totalsum - a[st1_count-1]
            st1_count = st1_count - 1
        
        if totalsum <= maxSum :
            print(st1_count,st2_count)
            arr.append(st1_count + st2_count)
    print(arr)        
    return max(arr)


#Queries with fixed length----------------

def solve(arr, queries):
    f_ans = []
    
    for x in queries :
        ans = []
        a1 = []
        for i in range(0,x) :
            a1.append(arr[i])
        ans.append(max(a1))

        for i in range(x,len(arr)) :
            del a1[0]
            a1.append(arr[i])
            ans.append(max(a1))
        f_ans.append(min(ans))

    
    return f_ans