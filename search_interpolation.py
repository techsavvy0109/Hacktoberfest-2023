list = [10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
def find(data):
    global list
    lo = 0
    hi = len(list) - 1
    mid = -1
    comparisons = 1
    index = -1
    while lo <= hi:
        print("\nComparison", comparisons)
        print("lo :", lo, ", list[", lo, "] =", list[lo])
        print("hi :", hi, ", list[", hi, "] =", list[hi])
        comparisons += 1
        #probe the mid point 
        mid = (int)(lo + (((hi - lo) / (list[hi] - list[lo])) * (data - list[lo])))
        print("mid =", mid)
        # data found
        if list[mid] == data:
            #if data is larger, data is in upper half 
            index = mid
            break
        else:
            # if data is smaller, data is in lower half 
            if list[mid] < data:
                lo = mid + 1
            else:
                hi = mid - 1
    print("\nTotal comparisons made:", comparisons - 1)
    return index
#find location of 33
location = find(33)
#if element was found
if location != -1:
    print("\nElement found at location:", (location+1))
else:
    print("Element not found.")
