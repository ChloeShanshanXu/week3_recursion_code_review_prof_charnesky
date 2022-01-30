def count_down(n):
    print(n)
    if n>0:
        count_down(n-1)

def count_down_loop(n):
    for value in range (n, 0, -1):
        print(value)

if __name__ =='__main__':
    count_down(8)
    count_down_loop(8)

def _binary_search(ls, num_to_find, start_index, end_index):
    if start_index>end_index:
        raise ValueError(str(num_to_find) + " is not in the list")
    mid=(start_index + end_index)//2
    if ls[mid]==num_to_find:
        print(mid)
    if ls[mid]<num_to_find:
        return _binary_search(ls, num_to_find, mid+1, end_index)
    return _binary_search(ls, num_to_find, start_index, mid-1)

def binary_search(ls, num_to_find):
    return _binary_search(ls, num_to_find,0,len(ls)-1)

if __name__ =='__main__':
    numbers=[2,54,23,93,2,43, 90, 203,4,8]
    numbers.sort()
    binary_search(numbers, 54)