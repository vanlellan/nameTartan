
import sys
import png
import colorsys


lastString = sys.argv[3]
lastList = [ord(x)-97 for x in lastString]
print(f"Last Name: {lastString}", lastList)
count = [ord(x)-96 for x in lastString]

middleString = sys.argv[2]
middleList = [ord(x)-97 for x in middleString]
print(f"Middle Name: {middleString}", middleList)

firstString = sys.argv[1]
firstList = [ord(x)-97 for x in firstString]
print(f"First Name: {firstString}", firstList)

maxLen = max(len(lastString), len(middleString), len(firstString))

while len(lastList) != maxLen:
    if len(lastList) > maxLen:
        lastList = lastList[:-1]
    elif len(lastList) < maxLen:
        lastList = lastList + lastList

while len(middleList) != maxLen:
    if len(middleList) > maxLen:
        middleList = middleList[:-1]
    elif len(middleList) < maxLen:
        middleList = middleList + middleList

while len(firstList) != maxLen:
    if len(firstList) > maxLen:
        firstList = firstList[:-1]
    elif len(firstList) < maxLen:
        firstList = firstList + firstList

#decimal HSV values
H = [x/25.0 for x in lastList]
S = [x/25.0 for x in middleList]
V = [x/25.0 for x in firstList]


#convert to RGB
rgb = [colorsys.hsv_to_rgb(a[0],a[1],a[2]) for a in zip(H,S,V)]

expanded = []
for j,c in enumerate(count):
    for i in [(x+1) for x in range(2*c)]:
        print(f"i={i}")
        expanded.append(rgb[j])

rev = list(expanded)
rev.reverse()
full = expanded+rev+expanded+rev

#generate tartan PNG
width = len(full)
height = width
img = []
for y in range(height):
    row = ()
    for x in range(width):
        #draw in 2 2 twill pattern with weft and weave, to make a good representation of the tartan
        if (x+y)%4 in (0,1):
            row = row + (int(full[x][0]*255),int(full[x][1]*255),int(full[x][2]*255))
        else:
            row = row + (int(full[y][0]*255),int(full[y][1]*255),int(full[y][2]*255))
    img.append(row)
with open(f"{firstString}-{middleString}-{lastString}.png", "wb") as outFile:
    w = png.Writer(width, height, greyscale=False)
    w.write(outFile, img)
