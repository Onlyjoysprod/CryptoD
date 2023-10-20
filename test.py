def partition(nums, low, high):
    # Выбираем средний элемент в качестве опорного
    # Также возможен выбор первого, последнего
    # или произвольного элементов в качестве опорного
    middle_number = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < middle_number:
            i += 1

        j -= 1
        while nums[j] > middle_number:
            j -= 1

        if i >= j:
            return j

        # Если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), меняем их местами
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low_id, high_id):
        if low_id < high_id:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low_id, high_id)
            print(split_index)
            _quick_sort(items, low_id, split_index)
            _quick_sort(items, split_index + 1, high_id)

    _quick_sort(nums, 0, len(nums) - 1)


# Проверяем, что оно работает
random_list_of_nums = [22, 5, 1, 18, 99, 0, 42, 13, 192, 13, 23]
quick_sort(random_list_of_nums)
print(random_list_of_nums)
