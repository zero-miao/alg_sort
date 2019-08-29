def heapify(lst, index, max_index):
    """在数组中, 以 index 为根, 构建大顶堆(最大长度为 max_index+1)
    时间复杂度:
        最优: 1
        最差: log(n)
    空间复杂度:
        最优: 1
        最差: log(n)
    """
    count = 1
    left = index * 2 + 1
    right = left + 1
    temp = lst[index]
    max_temp = temp
    max_i = index
    if left <= max_index and lst[left] > max_temp:
        max_temp = lst[left]
        max_i = left
    if right <= max_index and lst[right] > max_temp:
        max_temp = lst[right]
        max_i = right
    if max_i != index:
        lst[index], lst[max_i] = lst[max_i], lst[index]
        count += heapify(lst, max_i, max_index)
    return count


def build_heap(lst, end=None):
    """构建大顶堆: [0: end+1],
    时间复杂度:
        最优: n
        最差: n
    空间复杂度:
        最优: 1
        最差: log(n)
    """
    if end is None:
        end = len(lst) - 1
    for i in range((end - 1) // 2, -1, -1):
        # 以 i 为根的子堆.
        heapify(lst, i, end)


def heap_sort(lst):
    """堆排序

    时间复杂度:
        最优(所有数字一样大): n
        最差: n*log(n),
    空间复杂度:
        最优: 1
        最差: log(n)
    比较次数:
        最优: n
        最差: n * log(n)
    不稳定

    >>> lst = [7,6,5,4,3,2,1]
    >>> _ = heap_sort(lst)
    >>> lst
    [1, 2, 3, 4, 5, 6, 7]
    >>> lst = [6,8,4,2,4,6,8]
    >>> heap_sort(lst)
    >>> lst
    [2, 4, 4, 6, 6, 8, 8]
    >>> heap_sort([6,8,4,2,4,6,8,2])
    [2, 2, 4, 4, 6, 6, 8, 8]
    """
    build_heap(lst)
    count = 0
    # 现在 lst 是一个大顶堆. 去掉头.
    for end in range(len(lst) - 1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]
        count += heapify(lst, 0, end - 1)
    print(count)
    return lst
