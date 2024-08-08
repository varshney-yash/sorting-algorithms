l = [98,7,6,5,4,3,1,2,3,2,0,-1,-1,-2,100,-98]
n = len(l)

# need to traverse n-1 times; in each iteration 
# find out the index of minimum element and 
# swap it with the iteration number
def selection_sort(l):
    for i in range(n-1):
        min_i = i
        for j in range(i+1,n):
            if(l[min_i] > l[j]):
                min_i = j
        temp = l[min_i]
        l[min_i] = l[i]
        l[i] = temp
        
selection_sort(l)
print(l)
