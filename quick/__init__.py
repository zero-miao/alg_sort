def quick_sort_recursive(lst, start=0, end=None):
    """ 快速排序

    时间复杂度:
        最优: n*log(n), 假设其每次一分为 2(j 在正中间), T(n) = 2*T(n/2)+n => T(n) = n + 2*n/2 +...+ log(n)*n/log(n) = n*log(n)
        最差: n^2, 假设每次仅减少一个(j 在最边上), T(n) = T(n-1) + n => T(n) = n + n-1 +...+ 1 = n^2
    比较次数:
        最优: n*log(n), 每次循环的时候, 循环长度就是比较次数.
        最差: n^2, 同上.
    空间复杂度:
        最优: 同时间复杂度中最优, 需要递归 log(n) 次, 即栈空间 log(n)
        最差: 同时间复杂度中最差, 需要递归 n 次, 即栈空间 n.

    完全正序或逆序: 即为最差情况, (n^2, n)
    不稳定

    >>> lst = [7,6,5,4,3,2,1]
    >>> quick_sort_recursive(lst)
    [1, 2, 3, 4, 5, 6, 7]
    >>> lst
    [1, 2, 3, 4, 5, 6, 7]
    >>> quick_sort_recursive([6,8,4,2,4,6,8])
    [2, 4, 4, 6, 6, 8, 8]
    """
    if end is None:
        end = len(lst)

    if start >= end:
        return lst

    pivot = lst[start]
    j = start  # j 是最后一个小于等于 pivot 的元素的索引. i 用于遍历
    for index, item in enumerate(lst[start + 1:end], start + 1):
        if item < pivot:
            j += 1
            # 这里的操作就会改变 数组的稳定性: 即之前在前的元素, 最后不一定在前.
            lst[j], lst[index] = lst[index], lst[j]
    lst[j], lst[start] = lst[start], lst[j]
    quick_sort_recursive(lst, start=start, end=j)
    quick_sort_recursive(lst, start=j + 1, end=end)
    return lst
