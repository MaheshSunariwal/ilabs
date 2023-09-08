# Q1 square root

def squareroot(x) :
    for i in range (1,x +1) :
        
        if i*i > x :
            return i-1 

x = int(input())      
print(squareroot(x))

# testcase 

x = 27
output = 5

# --------------------------------------------

## Q2 two sorted arrays

def sorted(arr1,arr2,n1,n2) :
    arr3 = arr1 + arr2
    arr3.sort()
    arr1 = arr3[:n1]
    arr2 = arr3[n1 :]

    return arr1,arr2

# drivercode
n1 = int(input())
arr1 = []
for i in range(0,n1) :
    a = int(input())
    arr1.append(a)

n2 = int (input())
arr2 = []
for i in range (0,n2) :
    b = int(input())
    arr2.append(b)

print(sorted(arr1,arr2,n1,n2))

# -------------------------------------------


# Q-3 minimum number of platforms 

def minimumPlatform(n,arr,dep):
    # code here
    
    arr.sort()
    dep.sort()
    i = 0
    j = 0
    count = 0
    l = []
    while i < n and j < n :
        
        if arr[i] <= dep[j] :
            count = count + 1
            l.append(count)
            i = i + 1   
            
        else :
            count = count - 1
            l.append(count)
            j = j + 1  
            
    
    m = max(l)
    return m

# driver code
arrival = []
departure = []
n = int(input())
for i in range (0,n) :  
    a = int(input())
    arrival.append(a)

for i in range (0,n) : 
    b = int(input())
    departure.append(b)

print(minimumPlatform(n,arrival,departure))

# testcase 
n = 3
arrival = [900,915,920]
departure = [910,918,955]
output = 1