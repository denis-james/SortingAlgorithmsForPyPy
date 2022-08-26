def QuickSort(List,Testing=False):
    if Testing:
        EffortCounter=[0]
    lowerbound=0
    upperbound=len(List)-1
    def pivotPlacer(lb,ub):
        pivot=List[lb]
        l_pointer=lb
        h_pointer=ub
        while l_pointer<h_pointer:
            while List[l_pointer]<=pivot:
                if l_pointer==ub:
                    List[lb],List[ub]=List[ub],List[lb]
                    if Testing:
                        EffortCounter[0]+=1
                    return ub
                l_pointer+=1
            while List[h_pointer]>pivot:
                h_pointer-=1
            if h_pointer==lb:
                return lb
            if l_pointer<h_pointer:
                List[l_pointer],List[h_pointer]=List[h_pointer],List[l_pointer]
                if Testing:
                    EffortCounter[0]+=1
            else:
                List[h_pointer],List[lb]=List[lb],List[h_pointer]
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
    return List
