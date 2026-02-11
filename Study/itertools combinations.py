def combinations(arr,r):
    idx = list(range(r))

    while True:
        for i in reversed(range(r)):
            if idx[i] != i + len(arr) - r:
                break
        else:
            return
        
        yield (arr[i] for i in idx)

        for i in reversed(range(r)):
            if


combinations([1,2,3,4,5],3)


