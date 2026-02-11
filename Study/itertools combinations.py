def combinations(arr,r):
    idx = list(range(r))

    while True:
        for i in reversed(range(r)):
            if idx[i] != i + len(arr) - r:
                break
        else:
            return
        
        yield tuple(arr[i] for i in idx)

        for i in reversed(range(r)):
            if idx[i] != i + len(arr) - r:
                
                idx[i] += 1
                
                for j in range(i + 1, r):
                    idx[j] = idx[j - 1] + 1                    
                break


for i in combinations([1,2,3,4,5],3):
    print(i)
