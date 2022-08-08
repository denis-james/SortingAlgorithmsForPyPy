import math

def RadixSort(MainList,radix=10):
    if radix!=10:
        Differentbase={}
        if radix==2:
            for number in MainList:
                Differentbase[number]=int(bin(number).split('0b')[1])
        elif radix==8:
            for number in MainList:
                Differentbase[number]=int(oct(number).split('0o')[1])
        else:
            for number in MainList:
                i=number
                if i == 0:
                    Differentbase[i]=[0]
                digits = []
                while i:
                    digits.append(int(i % radix))
                    i//= radix
                Differentbase[number]=digits[::-1]

    def Sorter(List,PlaceOfSignificance):
        Buckets=[[] for i in range(radix)]
        print(PlaceOfSignificance)
        if radix!=10:
            if radix==2 or radix==8:
                for i in List:
                    newBase=Differentbase[i]
                    TheDigit=(newBase%(10**(PlaceOfSignificance))-newBase%(10**(PlaceOfSignificance-1)))/10**(PlaceOfSignificance-1)
                    Buckets[int(TheDigit)].append(i)
            else:
                for i in List:
                    if PlaceOfSignificance<=len(Differentbase[i]):
                        TheDigit=Differentbase[i][-PlaceOfSignificance]
                    else:
                        TheDigit=0
                    Buckets[int(TheDigit)].append(i)
        else:
            for i in List:
                TheDigit=(i%(10**(PlaceOfSignificance))-i%(10**(PlaceOfSignificance-1)))/10**(PlaceOfSignificance-1)
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
