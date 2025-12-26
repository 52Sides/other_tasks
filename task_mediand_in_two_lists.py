"""
Дано два отсортированных массива.
Какова оптимальная асимптотическая сложность алгоритма поиска медианы в массиве,
объединенном из этих двух?
"""

# асимптотическая сложность - O(log(min(n, m)))

def find_median_sorted_arrays(a: list[int], b: list[int]) -> float:
    if len(a) > len(b):
        a, b = b, a

    n, m = len(a), len(b)
    left, right = 0, n

    while left <= right:
        i = (left + right) // 2
        j = (n + m + 1) // 2 - i

        a_left = a[i - 1] if i > 0 else float("-inf")
        a_right = a[i] if i < n else float("inf")

        b_left = b[j - 1] if j > 0 else float("-inf")
        b_right = b[j] if j < m else float("inf")

        if a_left <= b_right and b_left <= a_right:
            if (n + m) % 2 == 1:
                return float(max(a_left, b_left))

            else:
                return (max(a_left, b_left) + min(a_right, b_right)) / 2

        elif a_left > b_right:
            right = i - 1
        else:
            left = i + 1

