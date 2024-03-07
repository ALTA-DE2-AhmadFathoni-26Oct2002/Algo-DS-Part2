def find_min_and_max(arr):
    if not arr:
          return None
    
    minimal = maximal = 0
    
    for j, k in enumerate (arr):
        if arr[j] < arr[minimal]:
                minimal = j
        if arr[j] > arr[maximal]:
                maximal = j
    min = arr[minimal]
    index_min = minimal
    max = arr[maximal]
    index_max = maximal

    result = (f"min: {min} index: {index_min} max: {max} index: {index_max}")
    return result



if __name__ == "__main__":
    print(find_min_and_max([5, 7, 4, -2, -1, 8]))
    # min: -2 index: 3 max: 8 index: 5
    print(find_min_and_max([2, -5, -4, 22, 7, 7]))
    # min: -5 index: 1 max: 22 index: 3
    print(find_min_and_max([4, 3, 9, 4, -21, 7]))
    # min: -21 index: 4 max: 9 index: 2
    print(find_min_and_max([-1, 5, 6, 4, 2, 18]))
    # min: -1 index: 0 max: 18 index: 5
    print(find_min_and_max([-2, 5, -7, 4, 7, -20]))
    # min: -20 index: 5 max: 7 index: 4