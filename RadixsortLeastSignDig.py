import math
def RadixSortLSD(MainList,radix=10):
    """
    Sorts the given list using RadixSort algorithm.
        Arguments:
            MainList: The list that's supposed to be sorted
            radix: The base using which radix sort would operate on the list
        Returns:
            ToBeReturned: The sorted list
    """
    def Sorter(List,PlaceOfSignificance):
        """
        Sorts the list by looking at the given place of significance.
            Arguments:
                List: The List supposed to be sorted.
                PlaceOfSignificance: the place of significance based on which the list is supposed to be sorted.
            Returns:
                TempSorted: Returns the partially sorted list
        """
        Buckets=[[] for i in range(radix)]
        for i in List:
            TheDigit=(i%(radix**(PlaceOfSignificance))-i%(radix**(PlaceOfSignificance-1)))/radix**(PlaceOfSignificance-1)
            Buckets[int(TheDigit)].append(i)
        TempSorted=[]
        for List in Buckets:
            TempSorted=TempSorted+List
        return TempSorted
    largest=max(MainList)
    largetstPlaceOfSignificance=math.floor(math.log(largest,radix))+1
    Sandbox=MainList
    for i in range(largetstPlaceOfSignificance):
        Sandbox=Sorter(Sandbox,i+1)
    ToBeReturned=[[],[]]
    for j in Sandbox:
        if j<0:
            ToBeReturned[0].append(j)
        else:
            ToBeReturned[1].append(j)

    return ToBeReturned[0]+ToBeReturned[1]
