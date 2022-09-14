import random
from Radixsort import RadixSort
from math import log2

def RandomList(length,limit1=0,limit2=10000):
    return [random.randint(limit1,limit2) for i in range(length)]

def PartiallyScrambled(length,Range=10000,fraction=.50):
    thelist=RadixSort([random.randint(0,Range) for i in range(length)],10)
    temp=list(thelist)
    positions=[random.randint(0,length-1) for i in range(int(length*fraction))]
    Sortedpositions=RadixSort(positions,10)
    for i in range(len(positions)):
        thelist[int(positions[i])]=temp[Sortedpositions[i]]
    del temp
    return thelist

def ScrambledTips(length,end,Range=10000,fraction=.30):
    thelist=RadixSort([random.randint(10,Range) for i in range(length)],10)
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
    Variety=RandomList(int(log2(length)),limit1,limit2)
    return [Variety[random.randint(0,len(Variety)-1)] for i in range(length)]

def Reversed(length,limit1=0,limit2=10000):
    return RadixSort(RandomList(length,limit1,limit2),10)[::-1]


#---------------------------------------------------------------------------------
