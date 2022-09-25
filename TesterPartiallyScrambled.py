from random import Random
from statistics import mean
import timeit
from RadixsortLeastSignDig import RadixSortLSD
from RadixSortMostSignDig import RadixSortMSD
from Quicksort import QuickSort
import ListGenerators

TimesList=[[] for i in range(10)]

for i in range(100):
    thelist=ListGenerators.PartiallyScrambled(1000000,Range=5000000,fraction=.4)
    time=timeit.timeit(setup="RadixSortLSD(thelist,2)",globals=globals())
    TimesList[0].append(time)
    print(i,"%/ done")
    time=timeit.timeit(setup="RadixSortMSD(thelist,2)",globals=globals())
    TimesList[1].append(time)
    time=timeit.timeit(setup="RadixSortLSD(thelist,8)",globals=globals())
    TimesList[2].append(time)
    time=timeit.timeit(setup="RadixSortMSD(thelist,8)",globals=globals())
    TimesList[3].append(time)
    time=timeit.timeit(setup="RadixSortLSD(thelist,10)",globals=globals())
    TimesList[4].append(time)
    time=timeit.timeit(setup="RadixSortMSD(thelist,10)",globals=globals())
    TimesList[5].append(time)
    time=timeit.timeit(setup="RadixSortLSD(thelist,16)",globals=globals())
    TimesList[6].append(time)
    time=timeit.timeit(setup="RadixSortMSD(thelist,16)",globals=globals())
    TimesList[7].append(time)
    time=timeit.timeit(setup="QuickSort(thelist)",globals=globals())
    TimesList[8].append(time)
    time=timeit.timeit(setup="thelist.sort()",globals=globals())
    TimesList[9].append(time)


with open("//mfs01/user01/SGDJAME4/MWSDesktop/MSc project/PartiallyScrambledTimesList.txt", "w") as output:
    output.write(str(TimesList))