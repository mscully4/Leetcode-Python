def permutations(lst):
    if len(lst) == 1:
        return [lst]

    results = []
    for i in range(len(lst)):
        obj = lst.pop(0)
        for perm in permutations(lst):
            results.append([obj] + perm)
        lst.append(obj)
    return results

print(permutations(["foo", "bar"]))