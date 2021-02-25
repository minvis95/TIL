# 분할을 해서 재귀적으로 활용
def quick_sort(numbers):
    N = len(numbers)
    if N <= 1:
        return numbers
    else:
        pivot = numbers[0]
        left, right = [], []

        for idx in range(1, N):
            if numbers[idx] > pivot:
                right.append(numbers[idx])
            else:
                left.append(numbers[idx])
        sorted_left = quick_sort(left)
        sorted_right = quick_sort(right)

        return [*sorted_left, pivot, *sorted_right]

numbers = [3, 9, 4, 7, 5, 0, 1, 6, 8, 2]
numbers = [4, 1, 2, 3]
def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    done = False

    while not done:
        # 왜 순서가 중요하지??
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1

        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]

    arr[start], arr[right] = arr[right], arr[start]
    return right


def quick_sort2(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort2(arr, start, pivot - 1)
        quick_sort2(arr, pivot + 1, end)
    return arr

print(numbers)
print(quick_sort(numbers))

print(numbers)
print(quick_sort2(numbers, 0, len(numbers)-1))
