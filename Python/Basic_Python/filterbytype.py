def filter_type(var):
#Integer
#If the integer is greater than or equal to 100 print "That's a big number!" If the integer is less than 100 print "That's a small number"
    if type(var) is int:
        if var >= 100:
            print "That's a big number!"
        else:
            print "That's a small number"
#String
#If the string is less than or equal to 50 characters print "Long sentenfasdfafce." If the string is shorter than 50 characters print "Short sentence."
    if isinstance(var, str):
        if len(var) >= 50:
            print "Long Sentence"
        else:
            print "Short Sentence"
#List
#If the length of the list is greater than or equal to 10 print "Big list!" If the list has fewer than 10 values print "Short list."
    if isinstance(var, list):
        if len(var) >=10:
            print "Big List!"
        else:
            print "Short List"

sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

filter_type(sI)
