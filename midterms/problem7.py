def f(a, b):
    return a > b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    d1keys = set(d1.keys())
    d2keys = set(d2.keys())
    commonkeys = d1keys.intersection(d2keys)
    differentkeys = d1keys.symmetric_difference(d2keys)
    fDict = {}
    diffDict = {}
    for key in commonkeys:
         fDict[key] = f(d1[key], d2[key])
    for key in differentkeys:
         if key in d1keys:
            diffDict[key] = d1[key]
         else:
            diffDict[key] = d2[key]

    return (fDict, diffDict)

d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}
print(dict_interdiff(d1, d2))
