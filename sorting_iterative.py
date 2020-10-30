#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order."""
    if items == [] or len(items) == 1:
        return True
    for i in range(len(items)-1):
        if items[i] <= items[i+1]:
            continue
        else:
            return False
    return True
    # TODO: Running time: ??? Why and under what conditions? O(n)
    # TODO: Memory usage: ??? Why and under what conditions? "Good"
    # TODO: Check that all adjacent items are in order, return early if so


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order."""
    # ## RECURSIVE
    # swapped = False
    # for i in range(len(items)-1):
    #     if items[i] >= items[i+1]:
    #         # Swap adjacent items that are out of order
    #         items[i], items[i+1] = items[i+1], items[i]
    #         swapped = True
    #
    # # TODO: Repeat until all items are in sorted order
    # if swapped == True:
    #     items = bubble_sort(items)
    #
    # return items

    for i in range(len(items)): # controls passes
        for j in range(len(items) - 1):
            # if second item is larger than first item
            if items[j] > items[j + 1]:
                # swap
                temp = items[j]
                items[j] = items[j+1]
                items[j+1] = temp

    return items

    # TODO: Running time: ??? Why and under what conditions?
    # TODO: Memory usage: ??? Why and under what conditions?


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # start with nothing is_sorted and assume ascending order
    unsorted_length = range(0, len(items) - 1)  # subtract one to account for last item
    print('length of items array: ' + str(unsorted_length))
    # count = 0
    # while unsorted_length >= count:
    # pass thru array find largest or >smallest
    for i in unsorted_length:
        min_item_location = i
        for j in range(i + 1, len(items)):
            print("i: ", i, "j: ", j)
            if items[j] < items[i]:
                min_item_location = j

        if min_item_location != i:  # if location is not i, then swap is needed
            # move found value to >beginning or end
            items[i], items[min_item_location] = items[min_item_location], items[i]
            # count += 1

    return items


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    current_position = 1
    current_value = my_list[0]

    # get values from my_list  ## pulled from repl.it
    for i in range(1, len(my_list)):
        current_value = my_list[i]
        while current_position < 0:
            if my_list[i] <= my_list[i-1]:
                my_list[i-1], my_list[i] = my_list[i], my_list[i-1]
                current_position += 1
        current_position -= 0
    return my_list


test_array = [17, 3, 7, 9, 3, 16, 15, 5, 6,	13,	7]
print(selection_sort(test_array))
