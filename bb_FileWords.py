"""The FileWords class is used to store the path of a file and a list of the
number of instances of each word used in that file. The other functions are used
to create the list from the raw text."""

def simplifyWord(wordIn):
    """Defines the rules of how words are normalised before being counted"""
    wordOut = wordIn.lower()
    wordOut = wordOut.rstrip(',;.:)]\"')
    wordOut = wordOut.lstrip(',;.:([\"')

    return wordOut

def processText(text):
    """Takes a string of text and returns a dictionary of all words it contains
    and their counts"""
    wordList = text.split()
    listOut = {}
    for i in range(len(wordList)):
        wordList[i] = simplifyWord(wordList[i])

    for j in range(len(wordList)):
        if wordList[j] in listOut:
            listOut[wordList[j]] += 1
        else:
            listOut[wordList[j]] = 1

    return listOut

class FileWords:
    """Stores the path of the file and a dictionary of all the words in that
    file and how many times they appear"""

    def __init__(self, path):
        self.m_path = path

    def createWordsFromTxt(self):
        fileIn = open(self.m_path, 'r')
        fullText = fileIn.read()
        self.m_words = processText(fullText)
