import math

def RadixMtoL(MainList,radix=10):
    if radix!=10:
        Differentbase={}
        if radix==2:
            for number in MainList:
                Differentbase[number]=int(bin(number).split('0b')[1])
        elif radix==8:
            for number in MainList:
                Differentbase[number]=int(oct(number).split('0o')[1])
        else:
            for number in MainList:
                i=number
                if i == 0:
                    Differentbase[i]=[0]
                digits = []
                while i:
                    digits.append(int(i % radix))
                    i//= radix
                Differentbase[number]=digits[::-1]

    largest=max(MainList)

    largetstPlaceOfSignificance=math.floor(math.log(largest,radix))+1
    def Orderchecker(aList):
        for i in range(len(aList)-1):
            if aList[i]>aList[i+1]:
                return False
        return True
    def Organizer(Box,PlaceOfSignificance):
        
        Organized=[[] for i in range(radix)]
        if radix!=10:
            if radix==2 or radix==8:
                for i in Box:
                    newBase=Differentbase[i]
                    TheDigit=(newBase%(10**(PlaceOfSignificance))-newBase%(10**(PlaceOfSignificance-1)))/10**(PlaceOfSignificance-1)
                    Organized[int(TheDigit)].append(i)
            else:
                for i in Box:
                    if PlaceOfSignificance<=len(Differentbase[i]):
                        TheDigit=Differentbase[i][-PlaceOfSignificance]
                    else:
                        TheDigit=0
                    Organized[int(TheDigit)].append(i)
        else:
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
