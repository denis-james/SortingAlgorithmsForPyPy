import math
def RadixMtoL(MainList,radix):
    largest=max(MainList)

    largetstPlaceOfSignificance=math.floor(math.log(largest,radix))+1
    def Orderchecker(aList):
        for i in range(len(aList)-1):
            if aList[i]>aList[i+1]:
                return False
        return True
    def Organizer(Box,PlaceOfSignificance):
        
        Organized=[[] for i in range(radix)]
        for i in Box:
            
            TheDigit=(i%(radix**(PlaceOfSignificance))-i%(radix**(PlaceOfSignificance-1)))/radix**(PlaceOfSignificance-1)
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
                if len(TheList[i])!=1 and PlaceOfSignificance!=1 and not(Orderchecker(TheList[i])):
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

theStack=RadixMtoL(TheIntegerList,10)
