def insert_sort(lst):
    """插入排序

    时间复杂度:
        最优: n
        最差: n^2
    空间复杂度:
        最优: 1
        最差: 1
    比较次数:
        最优: n
        最差: n^2

    最优: 全部正序, 每次的内层循环, 直接结束. (n, 1)
    最差: 全部逆序, 每次内层循环, 执行全部, (n^2, 1)
    稳定
    >>> lst = [7,6,5,4,3,2,1]
    >>> insert_sort(lst)
    [1, 2, 3, 4, 5, 6, 7]
    >>> lst
    [1, 2, 3, 4, 5, 6, 7]
    >>> insert_sort([6,8,4,2,4,6,8])
    [2, 4, 4, 6, 6, 8, 8]
    """
    for index, item in enumerate(lst[1:], 1):
        j = index - 1
        for temp in lst[index - 1::-1]:
            if item >= temp:
                lst[j + 1] = item
                break
            else:
                # 向后移动一位
                lst[j + 1] = temp
            j -= 1
        if j == -1:
            lst[0] = item
    return lst


def insert_sort_recursive(lst, start=0):
    """插入排序

    时间复杂度:
        最优: n
        最差: n^2
    空间复杂度:
        最优: n
        最差: n
    比较次数:
        最优: n
        最差: n^2

    最优: 全部正序, 每次的内层循环, 直接结束. (n, 1)
    最差: 全部逆序, 每次内层循环, 执行全部, (n^2, 1)
    稳定
    >>> lst = [7,6,5,4,3,2,1]
    >>> insert_sort_recursive(lst)
    [1, 2, 3, 4, 5, 6, 7]
    >>> lst
    [1, 2, 3, 4, 5, 6, 7]
    >>> insert_sort_recursive([6,8,4,2,4,6,8])
    [2, 4, 4, 6, 6, 8, 8]
    """
    # 前 start 个已经有序, 现在需要把 start+1 插入到前 start 个中.
    if start >= len(lst) - 1:
        return lst
    temp = lst[start + 1]
    index = start
    for item in lst[start::-1]:
        if temp >= item:
            lst[index + 1] = temp
            break
        else:
            lst[index + 1] = item
        index -= 1
    if index == -1:
        lst[0] = temp
    return insert_sort_recursive(lst, start + 1)
