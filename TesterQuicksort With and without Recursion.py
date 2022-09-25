
from Quicksort import QuickSort
from ListGenerators import RandomList
from Checker import ListOrderChecker
import timeit
Times=[]
for i in range(1000):
    thelist=RandomList(5000,-10000,10000)
    Times.append([
        timeit.timeit(setup="QuickSort(thelist)",globals=globals()),
        timeit.timeit(setup="thelist.sort()",globals=globals())
    ])


with open("C:/Users/denis/OneDrive/Desktop/M.Sc Project/QuicksortvsInbuiltTimes.txt", "w") as output:
    output.write(str(Times))