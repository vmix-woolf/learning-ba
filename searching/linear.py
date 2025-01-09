def linear_search(arr, x) -> int:
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def find(array, element):
    index = linear_search(array, element)
    if linear_search(array, element) == -1:
        print(f"Not found")
    else:
        print(f"Found and its index = {index}")


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    find(array, 4)
    find(array, 1)
    find(array, 0)
    find(array, 7)
