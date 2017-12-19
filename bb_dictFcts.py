"""Functions for manipulating dictionaries with numeric keys"""

def sortDictByNumVal(dictIn):
    """sort a dictionary by its positive numeric values"""
    
    sortedList = list(dictIn)
    
    for i in range(len(sortedList)):
        highest = 0
        highestIndex = 0
        for j in range(i, len(sortedList)):
            if dictIn[sortedList[j]] > highest:
                highest = dictIn[sortedList[j]]
                highestIndex = j

        temp = sortedList[i]
        sortedList[i] = sortedList[highestIndex]
        sortedList[highestIndex] = temp

    return sortedList

def addDicts(dict1, dict2):
    """Adds any keys from dict2 not already present to dict1, and adds the
in dict1 for shared keys"""
    for i in dict2:
        if i in dict1:
            dict1[i] += dict2[i]
        else:
            dict1[i] = dict2[i]
