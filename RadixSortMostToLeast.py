import math
def RadixMtoL(MainList,radix=10,Testing=False):
    if Testing:
        EffortCounter=[0]
    largestPlaceOfSignificance=len(str(max(MainList)))
    def Orderchecker(aList):
        for i in range(len(aList)-1):
            if aList[i]>aList[i+1]:
                return False
        return True
    def Organizer(Box,PlaceOfSignificance):
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
    origlen=len(MainList)
    MainList=Organizer(MainList,largestPlaceOfSignificance)
    for PlaceOfSignificance in range(largestPlaceOfSignificance-1,0,-1):
        assist=[]
        if origlen==len(MainList):
            break        
        for Chunk in MainList:
            if Orderchecker(Chunk):
                assist.append(Chunk)
            else:
                assist+=Organizer(Chunk,PlaceOfSignificance)
        MainList=assist
    ToBeReturned=[[],[]]
    for i in MainList:
        for j in i:
            if j<0:
                ToBeReturned[0].append(j)
            else:
                ToBeReturned[1].append(j)
    if Testing:
        return EffortCounter[0]
    return ToBeReturned[0]+ToBeReturned[1]
