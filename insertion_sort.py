l = [98,7,6,5,4,3,1,2,3,2,0,-1,-1,-2,100,-98]
n = len(l)

# array grows from 1 (ingle el is always sorted) to n; insert every key to its correct place in the growing array by shifting els to right till you find the correct place
def insertion_sort(l):
    for i in range(1,n):
        key = l[i]
        j = i-1
        while(j>=0 and key<l[j]):
            l[j+1] = l[j]
            j-=1
        l[j+1] = key
            
insertion_sort(l)
print(l)
