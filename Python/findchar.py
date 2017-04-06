def find_char(list, char):
    new = []
    for letter in list:
        if char in letter:
            new.append(letter)
    print new

list_o_things = ['hello','world','my','name','is','Anna', 'bird', 'is', 'the', 'word']
brought_to_you_by = 'e'

find_char(list_o_things, brought_to_you_by)
