data = [
    ["Abby", 58],
    ["Julia", 44],
    ["Jane", 31],
    ["Stephen", 76],
    ["Ryn", 82],
    ["Justin", 99],
    ["Caroline", 65],
    ["James", 87],
    ["Damon", 25],
    ["Elena", 76],
]


def bucketsort_hash(data):
    max_score = 100
    bucket = []
    bucket_num = lambda x: int(x / 33)

    for i in range(bucket_num(max_score) + 1):
        bucket.append([])

    for x in data:
        index = bucket_num(x[1])  # 以名字後的數字排序
        print(index)
        bucket[index].append(x)
        print(bucket[index])

    for i, flag in enumerate(bucket):
        if flag != []:
            bucket[i] = sorted(bucket[i], key=lambda x: x[1])

    index = 0
    for i in bucket:
        if i != []:
            for j in i:
                data[index] = j
                index += 1


# bucketsort_hash(data)

season = ["Spring", "Summer", "Autunm", "Winter"]
print(list(enumerate(season)))

