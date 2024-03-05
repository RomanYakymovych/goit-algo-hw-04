import timeit
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


# Генерування тестових даних
test_data_small = [random.randint(0, 100) for _ in range(100)]
test_data_medium = [random.randint(0, 1000) for _ in range(1000)]
test_data_large = [random.randint(0, 10000) for _ in range(10000)]


# Функція для тестування алгоритму
def test_sort_algorithm(algorithm, data):
    return timeit.timeit(lambda: algorithm(data.copy()), number=1)


# Вимірювання часу виконання
results = {}
for size, data in [
    ("Small", test_data_small),
    ("Medium", test_data_medium),
    ("Large", test_data_large),
]:
    for sort_algorithm in [
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Timsort (sorted)", sorted),
    ]:
        time = test_sort_algorithm(sort_algorithm[1], data)
        results[f"{sort_algorithm[0]} on {size} array"] = time

# Вивід результатів
for test, time in results.items():
    print(f"{test}: {time:.6f} seconds")
