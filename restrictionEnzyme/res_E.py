import math
import numpy as np
file = open("res_ezy.csv")

class ResE():
    def __init__(self, name, cutLst):
        self.name = name
        self.cutLst = cutLst
        self.cutDistLst = []

    def make_cutdist_lst(self):
        #makes a list of cutpoints' distance to original point
        len = 0
        for i in self.cutLst:
            len += i
            self.cutDistLst.append(len)
        #print(self.name, self.cutDistLst)

    @staticmethod
    def multiple_enz_cut(enz_lst):
        lst = []
        names = []
        for i in enz_lst:
            names.append(i.name)
            #print(i.cutDistLst)
            lst.extend(i.cutDistLst)
        lst.sort()
        #print(lst)
        #print(lst, "cut dist list")
        cutLst = ResE.dist2cut(lst)
        cutLst.sort()
        #print("enzymes: ", names, "cut: ", cutLst)
        #ResE.printEnzymeCustomized(names, cutLst)
        return names, cutLst

    @staticmethod
    def printEnzymeCustomized(names, cutLst):
        if 2392 in cutLst and 651 in cutLst and 415 in cutLst:
            print("enzymes: ", names, "cut: ", cutLst)

    @staticmethod
    def makeRangeLst():
        lengthMarks = [250, 500, 750, 1000, 1500, 2000, 2500, 3000, 4000, 5000, 6000, 8000, 10000]
        retLst = [(0, lengthMarks[0])]
        for i in range(1, len(lengthMarks)):
            retLst.append((lengthMarks[i - 1], lengthMarks[i]))
        retLst.append((lengthMarks[-1], math.inf))
        return retLst




    @staticmethod
    def dist2cut(lst):
        #takes a list of fragment size
        #return a list of cut distance to the 5' end of the original DNA
        ret = [lst[0]]
        for i in range(1, len(lst)):
            dis = lst[i] - lst[i-1]
            ret.append(dis)
        return ret

    @staticmethod
    def Name2Enz(nameLst, fullEnzLst):
        #use a list of name to generate a list of enzymes
        #nameLst: list of Enzyme names
        #fullEnzLst: list of ResE object containing all subjects of interest
        retLst = []
        for i in fullEnzLst:
            if i.name in nameLst:
                retLst.append(i)
        return retLst

    @staticmethod
    def Enz2Name(fullEnzLst):
        #use a list of ResE (restriction enzyme) objects to generate a list of strings of enzyme names
        retLst = []
        for i in fullEnzLst:
            retLst.append(i.name)
        return retLst

    def has_between(self, start, minlen, maxlen):
        #return 1 if has a fragment between minlen and maxlen, at or after the starting fragment; else return 0
        for i in self.cutLst[start:]:
            if i>minlen and i<maxlen:
                return 1
        return 0

    @staticmethod
    def has_between(lst, minlen, maxlen):
        for i in lst:
            if i>minlen and i<maxlen:
                return 1
        return 0

    @staticmethod
    def has_between_lst(cutLst, rangeLst):
        #takes a list of fragment sizes and a list of length size range (e.g. [[100, 250], [250, 500]])
        #return a dictionary of [size_range]: number of fragment
        dic = {}
        for i in rangeLst:
            i = tuple(i)
            dic[i] = 0
            for j in cutLst:
                if (j >= i[0] and j < i[1]) or (j <= i[0] and j >= i[1]):
                    dic[i] += 1
        return dic

def makeEnzLst():
    cnt = 0
    enz_Lst = []
    for line in file:
        if cnt != 0:
            new_enz = ResE('none', [])
            a = line.strip()
            lst = a.split(",")
            name = lst[0]
            lst1 = lst[1:len(lst)]
            new_enz.name = name

            for i in lst1:
                try:
                    temp = int(i)
                    new_enz.cutLst.append(temp)
                except ValueError:
                    pass
            enz_Lst.append(new_enz)
        cnt += 1
    return enz_Lst

def initialize():
    full_enz_Lst = makeEnzLst()
    for i in full_enz_Lst:
        i.make_cutdist_lst()
    return full_enz_Lst

'''
for i in enz_Lst:
    i.make_cutdist_lst()
for i in enz_Lst:
    print("Name: ", i.name, "; cut: ", i.cutDistLst, "\n \t frag: ", i.cutLst)

print(ResE.dist2cut([1, 2, 4, 6, 7]))
'''



full_enz_Lst = initialize()

enz = ResE.Name2Enz(["hindIII"], full_enz_Lst)
rangeLst = ResE.makeRangeLst()
print(rangeLst)
print(sorted(enz[0].cutDistLst))
print(ResE.multiple_enz_cut(enz))
'''for i in enz:
    lst = i.cutLst
    dic = ResE.has_between_lst(lst, rangeLst)
    print(dic)'''
'''ResE.multiple_enz_cut(enz)'''
fullLst = ResE.Enz2Name(full_enz_Lst)
for i in fullLst:
    #print(i)
    temp_lst = ResE.Name2Enz(['bglII', i], full_enz_Lst)
    #print(len(temp_lst), i) #wierd behavior if i is bglII itself
    names, cutLst = ResE.multiple_enz_cut(temp_lst)
    dic = ResE.has_between_lst(cutLst, rangeLst)
    lst1 = []
    flg1 = 0
    flg2 = 0
    flg3 = 0

    for i in cutLst:
        if i == 60 or i == 415 or i == 651:
            flg1 += 1 #should be 3
        if i > 651 and i < 2392:
            flg2 += 1 #should be 1
        if i > 2392 and i < 6557:
            flg3 += 1
    if flg1 == 3 and flg2 == 1 and flg3 ==2:
        print(names, cutLst)
    '''if dic[(2000, 2500)] + dic[(2500, 3000)] == 1:
        if dic[(2500, 3000)] + dic[(3000, 4000)] + dic[(4000, 5000)] == 3:
            print(names,"\n", dic)
            print(cutLst)'''
