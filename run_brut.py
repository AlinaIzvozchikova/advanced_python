from collections import namedtuple
from functools import lru_cache

CAPACITY = 400
Item = namedtuple('Item', 'name weight value')


def convert_to_item(value):
    return Item(value[0], int(value[1]), int(value[2]))


@lru_cache(maxsize=None)
def best_value(elem_iter, capacity):
    if elem_iter == 0:
        return 0
    if all_items[elem_iter - 1].weight > capacity:
        return best_value(elem_iter - 1, capacity)
    else:
        return max(
            best_value(elem_iter - 1, capacity),
            best_value(elem_iter - 1, capacity - all_items[elem_iter - 1].weight)
            + all_items[elem_iter - 1].value)


if __name__ == '__main__':

    with open('knapsack_items.txt') as f:
        lines = f.readlines()

    all_items = [convert_to_item(line.split(',')) for line in lines]

    knapsack_items = []

    for i in reversed(range(len(all_items))):
        if best_value(i + 1, CAPACITY) > best_value(i, CAPACITY):
            knapsack_items.append(all_items[i])
            CAPACITY -= all_items[i].weight

    knapsack_items = sorted(knapsack_items, key=lambda x: x.value, reverse=True)

    total_weight = 0
    max_value = 0
    for knapsack_item in knapsack_items:
        print(knapsack_item)
        total_weight += knapsack_item.weight
        max_value += knapsack_item.value

    print('\ntotal weight: ', total_weight)
    print('max value: ', max_value)
    print(best_value.cache_info())
