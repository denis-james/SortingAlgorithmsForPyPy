def QuickSort(theList,Testing=False):
    """
    Sorts the given list using the QuickSort Sorting algorithm. 
        Parameters:
            theList: The integer List that is supposed to be sorted
            Testing: A boolean variable that,
                if false, will return the Sorted list without calculating the Effort
                if true, will calculate and return the effort taken to sort the list only and not the sorted list itself. 
        Returns:
            SortedList: the sorted list(if Testing==False)
            EffortCounter[0]: the effort taken to sort the list(if Testing==True)
    """
    SortedList=list(theList)
    if Testing:
        EffortCounter=[0]
    lowerbound=0
    upperbound=len(SortedList)-1
    def pivotPlacer(lb,ub):
        """
        Places the pivot element in it's right position
            Arguments:
                lb,ub: The Indeces between which the pivot is supposed to be placed.
            Returns:
                h_pointer: the Index where the pivot is placed.
        """
        pivot=SortedList[lb]
        l_pointer=lb
        h_pointer=ub
        while l_pointer<h_pointer:
            while SortedList[l_pointer]<=pivot:
                if l_pointer==ub:
                    SortedList[lb],SortedList[ub]=SortedList[ub],SortedList[lb]
                    if Testing:
                        EffortCounter[0]+=1
                    return ub
                l_pointer+=1
            while SortedList[h_pointer]>pivot:
                h_pointer-=1
            if h_pointer==lb:
                return lb
            if l_pointer<h_pointer:
                SortedList[l_pointer],SortedList[h_pointer]=SortedList[h_pointer],SortedList[l_pointer]
                if Testing:
                    EffortCounter[0]+=1
            else:
                SortedList[h_pointer],SortedList[lb]=SortedList[lb],SortedList[h_pointer]
                if Testing:
                    EffortCounter[0]+=1
                return h_pointer
    partitions=[[lowerbound,upperbound]]
    while len(partitions)!=0:
        pivotposition=pivotPlacer(partitions[0][0],partitions[0][1])
        if pivotposition+1<partitions[0][1]:
            partitions.insert(1,[pivotposition+1,partitions[0][1]])
        if partitions[0][0]<pivotposition-1:
            partitions.insert(1,[partitions[0][0],pivotposition-1])
        del partitions[0]
    if Testing:
        return EffortCounter[0]
    return SortedList
