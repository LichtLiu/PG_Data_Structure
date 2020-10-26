# bucket resort 2
data2 = [
    ["Abby", 58, 92, 63],
    ["Julia", 44, 16, 58, 93],
    ["Jane", 31, 62, 93, 74],
    ["Stephen", 76, 94, 88, 99],
    ["Ryn", 82, 66, 77, 88],
    ["Justin", 99, 56, 78],
    ["Caroline", 65, 98, 100],
]


def Bucket_Sort2(data2):
    new_score_list = []
    for info in data2:
        total = 0
        for score in info:
            if type(score) == str:
                continue
            else:
                total += score
        new_score_list.append(int(total / (len(info) - 1)))

    new_name_list = []
    for i in data2:
        for j in i:
            if type(j) == str:
                new_name_list.append(j)
            else:
                continue
    data = []
    new_data = zip(new_name_list, new_score_list)
    for i in new_data:
        data.append(list(i))

    bucket = []
    for i in range(101):
        bucket.append([])

    for j in data:
        bucket[j[1]].append(j)

    index = 0
    result = []
    for i in bucket:
        if i != []:
            for j in i:
                result.append(j)
    print(result)


Bucket_Sort2(data2)

