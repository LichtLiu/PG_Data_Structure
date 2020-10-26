#Radix Sort
data = [100, 23, 23, 29, 34, 55, 66, 67, 78, 78, 79, 88, 89, 92, 96, 96]

def radix_sort(data):
    length = len(data) #16
    count = max(data) #100
    
    #用最大數判斷最大位元
    digit = 1
    while count > 9:
        count /= 10  # count = count/10 ,10 1
        digit += 1

    #digit = 3 #三位數

    tmp = []
    cur = 0
    for i in range(length):  # 資料的大小會決定桶子的數量，會是一個二維陣列
        tmp.append([0]*length)
    order = [0] * length
    print(order)

    if digit <= 9:
        '''use LSD(Least Significant digit) method'''
        n = 1
        while n <= max(data):
            for i in range(length):
                lsd = int(data[i]/n) % 10 #將資料用10來取個位數於數
                






print({(x,x*x):(x*x,x) for x in range(1,5,1)})

rec = {'name':'bob',
'jobs':['developer'],
'web':['www.bobs.org','www.bob2.org'],
'home':{'state':'overwork','zip':12345}}

print(rec['web'][1])



