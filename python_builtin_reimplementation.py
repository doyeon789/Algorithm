# max()
def max_(arr):
    m = arr[0]
    for x in arr:
        if x > m :
            m = x
    return m

# min()
def min_(arr):
    m = arr[0]
    for x in arr:
        if x < m:
            m =x
    return m

# sum()
def sum_(arr):
    total = 0
    for x in arr:
        total += x
    return total

# len()
def len_(arr):
    cnt = 0
    for _ in arr:
        cnt += 1
    return cnt

# count()
def count_(arr, target):
    cnt = 0
    for x in arr:
        if x == target:
            cnt += 1
    return cnt

# sort(), sorted()
def sort_(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# map()
def map_(func,arr):
    result = []
    for x in arr:
        result.append(func(x))
    return result

# zip()
def zip_(a, b):
    result = []
    n = min_(len(a), len(b))
    for i in range(n):
        result.append((a[i], b[i]))
    return result

# range()
def range_(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0

    if step == 0:
        raise ValueError("step은 0이 될 수 없습니다")

    i = start
    if step > 0:
        while i < stop:
            yield i
            i += step
    else:
        while i > stop:
            yield i
            i += step
