from collections import namedtuple

CAPACITY = 400
Item = namedtuple('Item', 'name weight value efficiency')


def convert_to_item(value):
    return Item(value[0],
                int(value[1]),
                int(value[2]),
                int(value[2]) / int(value[1]))


if __name__ == '__main__':

    with open('knapsack_items.txt') as f:
        lines = f.readlines()

    all_items = [convert_to_item(line.split(',')) for line in lines]

    knapsack_items = []

    sorted_items = sorted(all_items, key=lambda x: x.efficiency, reverse=True)
    current_capacity = 0

    for sorted_item in sorted_items:
        if current_capacity <= CAPACITY \
                and current_capacity + sorted_item.weight < CAPACITY:
            current_capacity += sorted_item.weight
            knapsack_items.append(sorted_item)

    total_weight = 0
    max_value = 0
    for knapsack_item in knapsack_items:
        print(knapsack_item)
        total_weight += knapsack_item.weight
        max_value += knapsack_item.value

    print('\ntotal weight: ', total_weight)
    print('max value: ', max_value)
