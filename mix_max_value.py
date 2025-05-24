from typing import List, Tuple


def find_min_max(arr: List[int]) -> Tuple[int, int]:
    if not arr:
        raise ValueError("Array cannot be empty")

    if len(arr) == 1:
        return arr[0], arr[0]
    elif len(arr) == 2:
        return (min(arr[0], arr[1]), max(arr[0], arr[1]))

    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])

    return (min(left_min, right_min), max(left_max, right_max))


if __name__ == "__main__":
    arr = [5, 14, 9, -7, 5, 33]
    minimum, maximum = find_min_max(arr)
    print(f"Min: {minimum}, Max: {maximum}")