name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def makeDictv2(arr1,arr2):
    i =0
    newList= []
    newDict = {}
    length=0
    if len(arr1)>len(arr2):
        length = len(arr)
    else:
        length - len(arr2)
    for index in range(len(arr1)):
        for items in arr1:
        #print arr2[index]
            newDict[arr1[index]] = arr2[index]
    print newDict
makeDictv2(name, favorite_animal)

def makeDictv2(arr1,arr2):
    newDict= {}
    if len(arr1)>len(arr2):
        length = len(arr1)
        big = arr1
        small = arr2
    else:
        length = len(arr2)
        big = arr2
        small = arr1

    for index in range(length):
        #for items in arr1:
        #print arr2[index]
        try:
            newDict[big[index]] = small[index]
        except IndexError:
            newDict[big[index]] = None
    print newDict
makeDictv2(name, favorite_animal)

##dictionaries printed according to python
##looks random to us and you would think it would print in the order it was put in-- but there that is not the case.
