def shell_sort(lst, gap=None):
    """希尔排序
    分组排序, 组内部插入排序:
    第一组: 复杂度 最优-组内正序(n, 1), 最差-组内倒序 (n^2, 1),
    第二组: 复杂度 最优-组内正序(n, 1), 最差-(每个元素最多与相邻的元素交换一次) (n, 1), (每次 step/2, 交换一次, step/3 交换两次)

    >>> lst = [7,6,5,4,3,2,1]
    >>> shell_sort(lst, 4)
    [1, 2, 3, 4, 5, 6, 7]
    >>> lst
    [1, 2, 3, 4, 5, 6, 7]
    >>> shell_sort([6,8,4,2,4,6,8])
    [2, 4, 4, 6, 6, 8, 8]
    >>> shell_sort([6,8,4,2,4,6,8,2])
    [2, 2, 4, 4, 6, 6, 8, 8]
    """
    l = len(lst)
    if gap is None and l > 3:
        gap = l // 3
    if gap < 1:
        gap = 1

    count = 0
    step = gap
    while step > 0:
        for i in range(gap):
            count += shell_insert_sort(lst, i, step)
        step //= 2
    print(count)
    return lst


def shell_insert_sort(lst, start, step):
    count = 0
    for i in range(start + step, len(lst), step):
        item = lst[i]
        for index in range(i - step, start - 1, -step):
            count += 1
            if lst[index] > item:
                lst[index + step] = lst[index]
                if index <= start - 1 + step:
                    lst[index] = item
            else:
                lst[index + step] = item
                break
    return count
