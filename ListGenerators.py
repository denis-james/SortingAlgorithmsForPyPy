
import random
from RadixsortLeastSignDig import RadixSortLSD
from math import log2

def RandomList(length,limit1=0,limit2=10000):
    return [random.randint(limit1,limit2) for i in range(length)]

def PartiallyScrambled(length,Range=10000,fraction=.5):
    thelist=RadixSortLSD([random.randint(0,Range) for i in range(length)],2)
    temp=list(thelist)
    ShuffledIndeces=[i for i in range(length)]
    random.shuffle(ShuffledIndeces)
    SortedShuffledIndeces=RadixSortLSD(ShuffledIndeces[:int(fraction*length)],2)
    for i in range(int(fraction*length)):
        temp[SortedShuffledIndeces[i]]=thelist[ShuffledIndeces[i]]
    return temp

def ScrambledTips(length,end,Range=10000,fraction=.30):
    thelist=RadixSortLSD([random.randint(10,Range) for i in range(length)],10)
    temp=thelist
    indexlimit=int(length*fraction)
    if end==1:
        indexes=[i for i in range(indexlimit)]
        random.shuffle(indexes)
    elif end==-1:
        indexes=[len(thelist)-1-i for i in range(indexlimit)]
        random.shuffle(indexes)
    
    for i in range(1,indexlimit):
        thelist[end*i]=temp[indexes[i]]
    del temp
    return thelist

def RepeatingEntries(length,limit1=0,limit2=1000):
    Variation=RandomList(int(log2(length)),limit1,limit2)
    return [Variation[random.randint(0,len(Variation)-1)] for i in range(length)]



def Reversed(length,limit1=0,limit2=10000):
    return RadixSortLSD(RandomList(length,limit1,limit2),10)[::-1]


#---------------------------------------------------------------------------------
