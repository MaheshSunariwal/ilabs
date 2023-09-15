

#valid_substring-----------------

def findMaxLen(S):
    stack=[]
    stack.append(-1)
    ans=0
    for i in range(len(S)):
        if S[i]=='(':
            stack.append(i)
        else :
            stack.pop()
            if len(stack) == 0 :
                stack.append(i)
            ans = max(ans,i-stack[-1])
    return ans


#kth-smallest element--------------

def negative(s) :
    for x in s :
        if x < 0 :
            return x
    return 0
def printFirstNegativeInteger( A, N, K):
    stk = []
    ans = []
    for i in range(0,K) :
        stk.append(A[i])
    ans.append(negative(stk))
        
    for i in range(K,N) :
        stk.append(A[i])
        del stk[0]
        ans.append(negative(stk))

    return ans


#remove k-digits------------

def removeKdigits(self, num, k):
    stk = []
    i = 0
    while i < len(num) :
        if stk == []   :
            stk.append(num[i])
            
            i = i + 1
            
        elif num[i] > stk[-1] :
            stk.append(num[i])
            
            i = i + 1
            
        elif num[i] < stk[-1] :
            stk.pop()
            k = k-1
            
        if num[i] == '0' and stk == [] :
            i = i + 1
            
        while k == 0 and i < len(num):
            stk.append(num[i])
            i = i + 1
    str = ''.join(stk)
    return str