from dataCleaningHelpers import *
from tilingHelpers import *
from objectDefinitions import *
from test import *

def main():
    myFile = open("poem.txt")
    otherFile = open("syllablizedPoemOneSyllablePerWord.txt")

    #No punctuation in words!
    listOfWords = readInRawPoem(myFile)
    listOfSyls = readInSyllablePoem(otherFile)
    masterListOfSyllables = makeMasterListOfSyllables(listOfSyls)
    listOfSylNodes = makeSylNodes(listOfSyls)

    for i, node in enumerate(listOfSylNodes):
        #AHHH CAN BE OPTIMIZED WITH TRIES OVER HASHMAP
        myOminoe = ominoe(6)
        myOminoe.reachableIndices+= listOfReachableIndices(i, 60)
        extendOminoe(myOminoe, i, listOfSylNodes)
        expandInAllDirections(myOminoe, listOfSylNodes)

    #let's take valid tiles from the ominoe objects and sort them
    sortedListOfTiles = []
    for validTile in listOfTiles:
        sortedListOfTiles.append(validTile.getIndicesInOminoe())

    sortedListOfTiles.sort(key=lambda x: x[0])
    true = 0
    for i,validTile in enumerate(sortedListOfTiles):
        valid = testForValidity(validTile)
        if valid:
            true+=1
        if valid:
            print("valid: ",validTile,i)
        else:
            print("invalid: ", validTile,i)
    print("total tiles enumerated: " + str(len(sortedListOfTiles)))
    print("valid tiles: " + str(true))




if __name__ == "__main__":
    main()
