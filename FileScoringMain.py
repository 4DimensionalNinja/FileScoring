#! python3
"""Read files in a target folder and output a list and count of the top 10 most
used words in each, followed by the top 10 most used words in all files scanned.
Takes the following arguments:
inputPath (defaults to 'Input')
outputPath (defaults to blank)
"""

import os, pprint, datetime, sys
from sys import argv
from bb_FileWords import FileWords
from bb_dictFcts import sortDictByNumVal, addDicts

def fileAllowed(file):
    """Determines which scanned files will be processed"""
    if file.is_file() and file.name.lower().endswith('.txt'):
        return True
    else:
        return False

if len(sys.argv) >= 2 and os.path.exists(argv[1]):
    inputPath = argv[1]
else:
    inputPath = 'Input'
if len(sys.argv) >= 3 and os.path.exists(argv[2]):
    outputPath = argv[2]
else:
    outputPath = ''

reportName = 'file_score'

fileList = []
errorList = []

#read all text files in the target folder
with os.scandir(inputPath) as l:
    for n in l:
        if n.is_file() and fileAllowed(n):
            fileList.append(FileWords(n.path))

                

for i in fileList:
    try:
        i.createWordsFromTxt()
    except:
        errorList.append(i)


dtString = datetime.datetime.today().strftime(r'%Y-%m-%d %H.%M.%S')
with open(reportName + ' ' + dtString + '.txt', 'w') as outputFile:
    masterList = {}

    for j in fileList:
        outputFile.write('Top 10 words in: ' + os.path.basename(j.m_path) + '\n')
        outputFile.write(j.m_path + '\n')
        try:
            scoreList = sortDictByNumVal(j.m_words)
            for k in range(min(10, len(scoreList))):
                outputFile.write(str(j.m_words[scoreList[k]]) \
                                 + ' ' + scoreList[k] + '\n')
            outputFile.write('\n\n')

            addDicts(masterList, j.m_words)
        except:
            outputFile.write('File could not be processed\n\n')
        j.m_words.clear()

    outputFile.write('Top 10 words overall: \n\n')
    scoreList = sortDictByNumVal(masterList)
    for k in range(min(10, len(scoreList))):
        outputFile.write(str(masterList[scoreList[k]]) \
                         + ' ' + scoreList[k] + '\n')

    if len(errorList):
        outputFile.write('\n\nThe following files could not be read:\n')
        for l in errorList:
            outputFile.write(l.m_path)
