def QuickSort(List):
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
                    return ub
                l_pointer+=1
            while List[h_pointer]>pivot:
                h_pointer-=1
            if h_pointer==lb:
                return lb
            if l_pointer<h_pointer:
                List[l_pointer],List[h_pointer]=List[h_pointer],List[l_pointer]
            else:
                List[h_pointer],List[lb]=List[lb],List[h_pointer]
                return h_pointer
    def Sorter(lb,ub):
        pivotPosition=pivotPlacer(lb,ub)
        if lb<(pivotPosition-1):
            Sorter(lb,pivotPosition-1)
        if (pivotPosition+1)<ub:
            Sorter(pivotPosition+1,ub)
    Sorter(lowerbound,upperbound)
    return List
