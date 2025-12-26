"""
Дан отсортированный, но циклически сдвинутый массив (например, [6, 7, 8, 1, 2, 3, 4, 5]).
Напишите функцию для поиска заданного элемента с эффективностью лучше O(n).
"""

def binary_search_mod(lst: list[int], target: int) -> int:
    left, right = 0, len(lst) - 1

    while left <= right:
        mid = (left + right) // 2

        if lst[mid] == target:
            return mid

        if lst[left] <= lst[mid]:
            if lst[left] <= target < lst[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if lst[mid] < target <= lst[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

if __name__ == "__main__":
    lst = [6, 7, 8, 1, 2, 3, 4, 5]
    assert binary_search_mod(lst, 3) == 5
    assert binary_search_mod(lst, 6) == 0
    assert binary_search_mod(lst, 8) == 2
    assert binary_search_mod(lst, 5) == 7


