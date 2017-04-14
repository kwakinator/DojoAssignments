def make_dict(arr1, arr2):
    new_dict= {}
    #code here
    combine = zip(arr1, arr2)
    new_dict = dict(combine)
    return new_dict

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

print make_dict(name, favorite_animal)
