def merge_sort(lst, start=0, end=None, merge=None):
    """堆排序

    时间复杂度: n*log(n),
    空间复杂度: n
    比较次数: n 有序, n^2 无序
    稳定

    >>> lst = [7,6,5,4,3,2,1]
    >>> _ = merge_sort(lst)
    >>> lst
    [1, 2, 3, 4, 5, 6, 7]
    >>> lst = [6,8,4,2,4,6,8]
    >>> _ = merge_sort(lst)
    >>> lst
    [2, 4, 4, 6, 6, 8, 8]
    >>> merge_sort([6,8,4,2,4,6,8,2])
    [2, 2, 4, 4, 6, 6, 8, 8]
    """
    l = len(lst)
    if end is None:
        end = l
    if merge is None:
        merge = [0] * l
    if start >= end - 1:
        return lst
    mid = (start + end) // 2
    merge_sort(lst, start, mid, merge)
    merge_sort(lst, mid, end, merge)
    # merge
    i, j = start, mid
    while i < mid and j < end:
        if lst[i] <= lst[j]:
            merge[i + j - mid] = lst[i]
            i += 1
        else:
            merge[i + j - mid] = lst[j]
            j += 1
    if i < mid:
        for i, item in enumerate(lst[i:mid], i):
            merge[i + j - mid] = item
    else:
        for j, item in enumerate(lst[j:end], j):
            merge[i + j - mid] = item
    lst[start:end] = merge[start:end]
    return lst
