import math
def RadixSort(MainList,radix):
    def Sorter(List,PlaceOfSignificance):
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
    return Sandbox
