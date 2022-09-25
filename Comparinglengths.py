
import timeit
from Quicksort import QuickSort
from RadixSortMostSignDig import RadixSortMSD
from RadixsortLeastSignDig import RadixSortLSD

from ListGenerators import RandomList

TimeList=[[],[],[]]
for i in range(1,1001):
    print(i)
    thelist=RandomList(i*1000)
    TimeList[0].append(QuickSort(thelist,True))
    TimeList[1].append(RadixSortMSD(thelist,Testing=True))
    with open("//mfs01/user01/SGDJAME4/MWSDesktop/MSc project/CompairingEfforts.txt", "w") as output:
        output.write(str(TimeList))
print(TimeList)

