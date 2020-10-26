# Bucket Sort

# as we want to sort these score
data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]

# Prepare Buckets

max_score = 100  # The highest score is 100
bucket = []
for i in range(max_score + 1):  # prepare 101 buckets (plus 0 score)
    bucket.append(0)  # [0,0,0,0,0........0] to 101

# Sort Score
for score in data:
    bucket[score] = bucket[score] + 1  # bucket[23] = bucket[23] + 1

# Read Score
index = 0
for i in range(len(bucket)):  # 101
    if bucket[i] != 0:  # bucket[23] = 2
        for j in range(bucket[i]):  # range(2)
            data[index] = i  # data[0] = 23
            index += 1

