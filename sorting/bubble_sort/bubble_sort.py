def bubble_sort(lst) -> list:
    length = len(lst)
    for i in range(length - 1):
        for j in range(0, length - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    
    return lst


print(bubble_sort([95, 14, 3, 22, 1, 101, 34, 20, 56, 39, 85, 90, 77, 12, 0, 75]))
