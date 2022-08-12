
import random
import timeit
from Radixsort import RadixSort


def RandomList(length,limit2=10000,limit1=0):
    return [random.randint(limit1,limit2) for i in range(length)]

def PartiallyScrambled(length,Range=10000,fraction=.50):
    thelist=RadixSort([random.randint(0,Range) for i in range(length)])
    temp=list(thelist)
    positions=[random.randint(0,length-1) for i in range(int(length*fraction))]
    Sortedpositions=RadixSort(positions)
    for i in range(len(positions)):
        thelist[int(positions[i])]=temp[Sortedpositions[i]]
    del temp
    return thelist

def ScrambledTips(length,end,Range=10000,fraction=.30):
    thelist=RadixSort([random.randint(10,Range) for i in range(length)])
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

def RepeatingEntries(length,limit2=1000,limit1=0):
    appendable=RandomList(int(length*.1),limit2,limit1)
    tobeshuffeled=[]
    for i in range(10):
        tobeshuffeled=tobeshuffeled+appendable
    random.shuffle(tobeshuffeled)
    return tobeshuffeled

def Reversed(length,limit2,limit1):
    return RadixSort(RandomList(length,limit2,limit1))[::-1]


#---------------------------------------------------------------------------------
