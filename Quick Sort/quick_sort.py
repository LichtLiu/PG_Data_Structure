# Quick Sort
# 2019/10/18  
sequence = [5, 4, 7, 6, 2, 3, 1]


def quicksort(sequence):
    if len(sequence) <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    item_greater = []
    item_lower = []

    for i in sequence:
        if i > pivot:
            item_greater.append(i)
        else:
            item_lower.append(i)
    print(item_lower + [pivot] + item_greater)
    return quicksort(item_lower) + [pivot] + quicksort(item_greater)


x = quicksort(sequence)
print(x)
