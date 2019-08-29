def bubble_sort(lst):
    """冒泡排序

    时间复杂度:
        最优: n^2
        最差: n^2
    空间复杂度:
        最优: 1
        最差: 1
    比较次数:
        最优: n^2
        最差: n^2

    无论什么顺序, 都是 (n^2, 1)

    稳定
    >>> lst = [7,6,5,4,3,2,1]
    >>> bubble_sort(lst)
    [1, 2, 3, 4, 5, 6, 7]
    >>> lst
    [1, 2, 3, 4, 5, 6, 7]
    >>> bubble_sort([6,8,4,2,4,6,8])
    [2, 4, 4, 6, 6, 8, 8]
    """
    count = 0
    for i in range(len(lst), 0, -1):
        for index, item in enumerate(lst[1:i], 1):
            count += 1
            if item < lst[index - 1]:  # 这里不加等于号, 就能保持稳定.
                lst[index - 1], lst[index] = lst[index], lst[index - 1]
    print(count)
    return lst


def bubble_sort_recursive(lst, end=None):
    """冒泡排序

    时间复杂度:
        最优: n^2
        最差: n^2
    空间复杂度:
        最优: n, 递归 n 次. 栈空间 n
        最差: n, 同上.
    比较次数:
        最优: n^2
        最差: n^2

    无论什么顺序, 都是 (n^2, n)

    稳定
    >>> lst = [7,6,5,4,3,2,1]
    >>> bubble_sort_recursive(lst)
    [1, 2, 3, 4, 5, 6, 7]
    >>> lst
    [1, 2, 3, 4, 5, 6, 7]
    >>> bubble_sort_recursive([6,8,4,2,4,6,8])
    [2, 4, 4, 6, 6, 8, 8]
    """
    if end is None:
        end = len(lst)
    if end == 0:
        return lst
    for index, item in enumerate(lst[1:end], 1):
        if item < lst[index - 1]:  # 这里不加等于号, 就能保持稳定.
            lst[index - 1], lst[index] = lst[index], lst[index - 1]
    return bubble_sort_recursive(lst, end - 1)
