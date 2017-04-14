def draw_stars(x):
    for item in x:
        num_chars = ''
        if type(item) is int:
            for char in range(0, item):
                num_chars += "*"
        else:
            for char in range(0, len(item)):
                num_chars += item[0].lower()
        print num_chars

x = [4, 6, 1, 3, 5, 7, 25]
y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)
draw_stars(y)

def stars(x):
    for num in x:
        print "*" * num

def drawStars(x):
    for item in x:
        if type(item) is int:
            print "*" * item
        elif type(item) is str:
            num_chars = len(item)rfd
            char = item[0].lower()
            print num_chars * char

x = [6, 1, 4, 5, 7, 20]
y = [2, "Happy", 1, "Grumpy", 5, 7, "422"]
stars(x)
drawStars(y)
