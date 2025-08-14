import heapq

def find_second_largest_heap(arr):
    if len(arr) < 2:
        return None
    # nlargest(k, iterable) returns a list with the k largest elements
    top_two = heapq.nlargest(2, list(set(arr))) 
    if len(top_two) < 2:
        return top_two[0]
    return top_two[1]

my_list = [20, 20, 20]
second_largest = find_second_largest_heap(my_list)
print(f"The second largest number is: {second_largest}")