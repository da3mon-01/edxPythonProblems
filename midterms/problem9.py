def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    newList = []
    for i in aList:
        if isinstance(i,list):
           newList.extend(flatten(i))
        else:
           newList.append(i)
    return newList


aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten(aList))
