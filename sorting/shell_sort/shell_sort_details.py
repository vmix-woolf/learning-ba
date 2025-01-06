def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        print(f"GAP: =============={gap}===================")
        for i in range(gap, n):
            temp = arr[i]
            j = i
            print(f"i: ----------------- {i} ----------------")
            print(f"Список на початку ітерації {i}: {arr}")
            print(f"j: {j}, temp: {temp}, gap: {gap}")
            print(f"Порівнюємо елементи: {arr[j - gap]} > {temp}")
            while j >= gap and arr[j - gap] > temp:
                print(f"Виконано обмін в циклу while: значення {arr[j - gap]} замінило {arr[j]}")
                arr[j] = arr[j - gap]
                print(f"Список змінився j: {j}: {arr}")
                j -= gap
                print(f"Змінили j вліво: {j}")
            print(f"В кінці циклу for: значення {temp} замінило {arr[j]}")
            arr[j] = temp
            print(f"Список на кінець ітерації {i}: {arr}")
        gap //= 2
        if gap == 0:
            print("Сортування завершено")
    return arr

numbers = [5, 3, 8, 4, 2]
# numbers = [64, 34, 25, 12, 22, 11, 90]
print(shell_sort(numbers))
