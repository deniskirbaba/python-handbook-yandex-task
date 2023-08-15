def merge_sort(arr):
    global true_len 
    if 'true_len' not in globals():
        true_len = len(arr)

    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        if k != len(arr):
            if i == len(L):
                while j != len(R):
                    arr[k] = R[j]
                    k += 1
                    j += 1
            else:
                while i != len(L):
                    arr[k] = L[i]
                    k += 1
                    i += 1
        
        if k == true_len:
            return arr


result = merge_sort([3, 1, 5, 3])
print(result)