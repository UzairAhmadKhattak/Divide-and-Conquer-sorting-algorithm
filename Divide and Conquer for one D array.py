numlist = [4,2,3,1,0]

def mergesort(numlist):
    
    if len(numlist) > 1:
        mid = int(len(numlist)/2)
        left = numlist[:mid]
        right = numlist[mid:]
        
        mergesort(left)
        mergesort(right)
        
        # merge start from here
        
        i = 0 
        j = 0
        k = 0
        
        while i < len(left) and j< len(right):
            
            if left[i] < right [j]:
                numlist[k] = left[i]
                i += 1
            else:
                numlist[k] = right[j]
                j += 1
            
            k += 1
            
        while i < len(left):
            
            numlist[k] = left[i]
            i += 1
            k += 1
        
        while j< len(right):
            
            numlist[k] = left[j]
            i += 1
            k += 1
    
    return numlist

print(mergesort(numlist))
