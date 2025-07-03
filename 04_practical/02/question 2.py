def find_max(lst):
    if not lst:
        return None
    largest = lst[0]
    for num in lst[1:]:
        if num > largest:
            largest = num
    return