# Q-1 palindrome string

def palindrome (str) :
    
    reverse = str[::-1]
    if reverse == str :
        return 1
    else :
        return 0

# driver code

str = input() 
print(palindrome (str))

# testcase
str = 'mam'
output = 1

#--------------------------------
# Q-2 array of size n-1

def array(arr,n) :
    sum = 0
    for i in range(1,n+1) :
        sum = sum + i
    add = 0
    for i in range (0,n-1) :
        add = add + arr[i]
    diff = sum  - add

    return diff

# driver code
n = int(input())
arr = []
for i in range(0,n-1) :
  a = int(input())
  arr.append(a)
print(arr)
print(array(arr,n))

# testcase
n = 4
arr = [1,2,4]
output = 3

# ----------------------
# Q-3 pooja
def function(AB,X) :
    net = AB - X - 0.5
    if X% 5 == 0 and net > 0 :
        AB = net
        return 'transaction completed',AB
    elif X % 5 != 0 and net> 0 :
        return 'not multiple of 5'

    elif AB< X :
        return AB


AB = int(input('account balance :'))
X = int (input('you wish to withdraw :'))

print(function(AB,X))