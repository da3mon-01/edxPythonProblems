def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    lAlen = len(listA)
    summa = 0
    for i in range(lAlen):
        summa = summa + (listA[i] * listB[i])
    return summa

listA = [1, 2, 3]
listB = [4, 5, 6]
print(dotProduct(listA, listB))  
