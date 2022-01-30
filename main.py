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

    mid=(start_index + end_index)//2
    if ls[mid]==num_to_find:
        return mid
    if ls[mid]<num_to_find:
        return _binary_search(ls, num_to_find, mid+1, end_index)
    return _binary_search(ls, num_to_find, start_index, mid-1)



def binary_search(ls, num_to_find):
    return _binary_search(ls, num_to_find,0,len(ls)-1)

if __name__ =='__main__':
    numbers=[2,54,23,93,7,43, 90, 203,4,8]
    numbers.sort()
    print(numbers)
    print("number is at " + str(binary_search(numbers, 54)) + " place of the list")

def iterative_binary_search(ls,num_to_find):
    start_index = 0
    end_index=len(ls)-1
    while start_index < end_index:
        mid = (start_index + end_index)//2
        if ls[mid] < num_to_find:
            start_index=mid+1
        if ls[mid] > num_to_find:
            end_index=mid-1
    return start_index

#    while start_index <= end_index:
 #       mid = (start_index + end_index)//2
  #      if ls[mid]== num_to_find:
   #         return mid
    #        quit
     #   if ls[mid]> num_to_find:
      #      end_index=mid-1
       # else:
        #    start_index = mid+1

if __name__ =='__main__':
    numbers=[2,54,23,93,7,43, 90, 203,4,8]
    numbers.sort()
    print(iterative_binary_search(numbers, 54))
    print("number is at " + str(iterative_binary_search(numbers, 54)) + " place of the list")
