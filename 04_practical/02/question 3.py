def find_smallest(lst):
    if not lst:
        return None
    smallest = lst[0]
    for num in lst[1:]:
        if num < smallest:
            smallest = num