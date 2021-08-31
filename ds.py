lst = [3, 1, 6, 4, 0]

def mergesort(l):
    if len(l) == 1:
        return [l[0]]

    half = int(len(l) / 2)
    a = l[:half]
    b = l[half:]

    c = mergesort(a)
    d = mergesort(b)

    return merge(c, d)

def merge(a, b):
    result = []
    
    while len(a) and len(b):
        if a[0] <= b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))

    while len(a):
        result.append(a.pop(0))
    
    while len(b):
        result.append(b.pop(0))

    return result

print(mergesort(lst))
