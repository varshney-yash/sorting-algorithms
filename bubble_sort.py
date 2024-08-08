l = [98,7,6,5,4,3,1,2,3,2,0,-1,-1,-2,100,-98]
n = len(l)

# n-1 iterations; for each iteration swap till 
# the largest element is pushed towards the end, 
# no swap means array got sorted break out
def bubble_sort(l):
    for i in range(n-1):
        swap = False
        for j in range(n-i-1):
            if(l[j]>l[j+1]):
                swap = True
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
        if not swap:
            break
            
bubble_sort(l)
print(l)
