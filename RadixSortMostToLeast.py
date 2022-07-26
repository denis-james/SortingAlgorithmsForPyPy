def RadixMtoL(MainList):
    largest=max(MainList)

    largetstPlaceOfSignificance=len(str(largest))
    def Orderchecker(aList):
        for i in range(len(aList)-1):
            if aList[i]>aList[i+1]:
                return False
        return True
    def Organizer(Box,PlaceOfSignificance):
        
        if Orderchecker(Box):
            return Box
        Organized=[[] for i in range(10)]
        for i in Box:
            
            TheDigit=(i%(10**(PlaceOfSignificance))-i%(10**(PlaceOfSignificance-1)))/10**(PlaceOfSignificance-1)
            Organized[int(TheDigit)].append(i)
        ToBeReturned=[]
        for i in Organized:
            if len(i)!=0:
                ToBeReturned.append(i)
        del Organized
        return ToBeReturned
        
    def Stacker(TheList,PlaceOfSignificance):
        TheList=Organizer(TheList,PlaceOfSignificance)
        if type(TheList[0])==list:
            for i in range(len(TheList)):
                if len(TheList[i])!=1 and PlaceOfSignificance!=1:
                    TheList[i]=Stacker(TheList[i],PlaceOfSignificance-1)
        return TheList
    def StackStraightner(TheList,ToBeReturned):
        for i in TheList:
            if type(i[0])==int:
                ToBeReturned=ToBeReturned+i
            else:
                ToBeReturned=StackStraightner(i,ToBeReturned)
        return ToBeReturned
    return StackStraightner(Stacker(MainList,largetstPlaceOfSignificance),[])