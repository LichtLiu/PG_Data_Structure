# bubble sort
data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
# len(data) 16


def bubble_sort(data):
    for length in range(len(data) - 2):  # 頭是0尾14
        for i in range(len(data) - length - 1):  # 0, 1, 2, 3...
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
            else:
                continue
    print(data)


bubble_sort(data)
