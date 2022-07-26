def RadixSort(MainList):
    def Sorter(List,PlaceOfSignificance):
        Buckets=[[] for i in range(10)]
        for i in List:
            TheDigit=(i%(10**(PlaceOfSignificance))-i%(10**(PlaceOfSignificance-1)))/10**(PlaceOfSignificance-1)
            Buckets[int(TheDigit)].append(i)
        TempSorted=[]
        for List in Buckets:
            TempSorted=TempSorted+List
        return TempSorted
    largest=max(MainList)
    largetstPlaceOfSignificance=len(str(largest)
    Sandbox=MainList
    for i in range(largetstPlaceOfSignificance):
        Sandbox=Sorter(Sandbox,i+1)
    return Sandbox




