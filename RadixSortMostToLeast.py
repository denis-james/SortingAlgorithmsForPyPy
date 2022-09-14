import math
def RadixMtoL(MainList,radix=10,Testing=False):
    """
    Sorts the given list using RadixSort algorithm.
        Arguments:
            MainList: The list that's supposed to be sorted
            radix: The base using which radix sort would operate on the list
            Testing: A boolean variable that,
                if false, will return the Sorted list without calculating the Effort
                if true, will calculate and return the effort taken to sort the list only and not the sorted list itself. 

        Returns:
            SortedList: the sorted list(if Testing==False)
            EffortCounter[0]: the effort taken to sort the list(if Testing==True)
    """

    if Testing:
        EffortCounter=[0]
    largest=max(MainList)
    largetstPlaceOfSignificance=math.floor(math.log(largest,radix))+1
    def Orderchecker(aList):
        """
        Checks the order of the given list
            Arguments:
                aList: a List of Integers
            Returns:
                True: if the list is already sorted
                False: otherwise
        """
        for i in range(len(aList)-1):
            if aList[i]>aList[i+1]:
                return False
        return True
    def Organizer(Box,PlaceOfSignificance):
        """
        Partitions the list based solely on the given place of significance.
            Arguments:
                List: The List supposed to be partitioned.
                PlaceOfSignificance: the place of significance based on which the list is supposed to be sorted.
            Returns:
                TempSorted: Returns the partially sorted list
        """
        Organized=[[] for i in range(radix)]
        for i in Box:
            TheDigit=(i%(radix**(PlaceOfSignificance))-i%(radix**(PlaceOfSignificance-1)))/radix**(PlaceOfSignificance-1)
            if Testing:
                EffortCounter[0]+=1
            Organized[int(TheDigit)].append(i)
        ToBeReturned=[]
        for i in Organized:
            if len(i)!=0:
                ToBeReturned.append(i)
        del Organized
        return ToBeReturned
        
    def Stacker(TheList,PlaceOfSignificance):
        """
        Creates a stack, segregating the whole list into a list that is multiple layers deep, 
            Argument:
                TheList: The list supposed to be stacked.
                PlaceOfSignificance: the place of significance based on which the list is supposed to be stacked.
            Returns:
                TheList: Given list but segregated into a multidimensional array based on it's radix.
        """
        TheList=Organizer(TheList,PlaceOfSignificance)
        if type(TheList[0])==list:
            for i in range(len(TheList)):
                if len(TheList[i])!=1 and PlaceOfSignificance!=1 and not(Orderchecker(TheList[i])):
                    TheList[i]=Stacker(TheList[i],PlaceOfSignificance-1)
        return TheList
    
    def StackStraightner(TheList,ToBeReturned):
        """
        Reduces the depth of the list by joining all the individual lists layer by layer.
        """
        for i in TheList:
            if type(i[0])==int:
                ToBeReturned=ToBeReturned+i
            else:
                ToBeReturned=StackStraightner(i,ToBeReturned)
        return ToBeReturned
    if Testing:
        StackStraightner(Stacker(MainList,largetstPlaceOfSignificance),[])
        return EffortCounter[0]
    return StackStraightner(Stacker(MainList,largetstPlaceOfSignificance),[])
