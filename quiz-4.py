#Q1 1 max_heap
def max_heap(arr,n,i):
    largest = i
    left = 2*i+1
    right = 2*i+2

    if left<n and arr[largest]< arr[left]:
        largest = left
    elif right<n and arr[largest]<arr[right]:
        largest=right
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        max_heap(arr,n,largest)
    return arr

# # drivercode

n = int(input())
arr= []

for i in range (0,n) :
    a = int(input())
    arr.append(a)

for i in range(n//2,-1,-1) :
    (max_heap(arr,n,i))

arr_max = (max_heap(arr,n,i))
print(max_heap(arr,n,i))

#---------------------------------------

#Q1 2 min_heap
def min_heap(arr,n,i):
    smallest = i
    left = 2*i+1
    right = 2*i+2

    if left<n and arr[smallest]> arr[left]:
        smallest = left
    elif right<n and arr[smallest]>arr[right]:
        smallest=right
    if smallest!=i:
        arr[i],arr[smallest]=arr[smallest],arr[i]
        min_heap(arr,n,smallest)
    return arr

# drivercode

n = int(input())
arr= []

for i in range (0,n) :
    a = int(input())
    arr.append(a)

for i in range(n//2,-1,-1) :
    (min_heap(arr,n,i))

arr_min = (min_heap(arr,n,i))
print(min_heap(arr,n,i))




#------------------------------------------------

#Q1 3 add element

def add_element(n,n1,arr) :
    arr.append(n1)
    n = n +1
    for i in range(n//2,-1,-1) :
        (min_heap(arr,n1,i))

    print(min_heap(arr,n,i))


n1 = int(input())
add_element(n1,arr)

#-----------------------------------------------
# # Q1 4 pop smallest from heap

arr_min.remove(arr_min[0])
print(arr_min)



#------------------------------------------
# Q1 5 pop largest from max_heap

arr_max.remove(arr_max[0])













