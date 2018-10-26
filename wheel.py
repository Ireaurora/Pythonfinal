sampleText = ("As Python's creator, I'd like to say a few words about its "+
              "origins, adding a bit of personal philosophy.\n"+
              "Over six years ago, in December 1989, I was looking for a "+
              "'hobby' programming project that would keep me occupied "+
              "during the week around Christmas. My office "+
              "(a government-run research lab in Amsterdam) would be closed, "+
              "but I had a home computer, and not much else on my hands. "+
              "I decided to write an interpreter for the new scripting "+
              "language I had been thinking about lately: a descendant of ABC "+
              "that would appeal to Unix/C hackers. I chose Python as a "+
              "working title for the project, being in a slightly irreverent "+
              "mood (and a big fan of Monty Python's Flying Circus).")



punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''


array = []
for char in sampleText:
    if char not in punctuations:
        char = list(char)
        array = array + char

def findingspaces(array):
    newarray = []
    a = ' '
    for index in range(len(array)):
        if array[index] == a:
            index = str(index)
            newarray.append(int(index))
    return newarray

print(array)

newarray = findingspaces(array)
print(newarray)


def joining(newarray, array):
    result = []
    i = 0
    size = len(newarray)
    for i in newarray:
        new = newarray[i]
        next = newarray[i+1]
        print(''.join(array[new:next]))


joining(newarray,array)
