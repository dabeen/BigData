from konlpy.tag import Komoran
from collections import Counter
import time


def openFile(filePath):
    lines = None
    with open(filePath) as f:
        try:
            lines = f.read().splitlines()
        except:
            f.close()
    return lines


def konlpykomo(inputSentence: str, sentenceList: list) -> dict:
    komo = Komoran()
    sentenceDict = dict()

    inputPos = komo.pos(inputSentence)
    inputPosCount = Counter(inputPos)
    inputLen = len(inputPosCount)

    for line in sentenceList:
        if line == '':
            continue
        sentencePos = komo.pos(line)
        sentencePosCount = Counter(sentencePos)
        sentenceLen = len(sentencePosCount)

        if sentenceLen > inputLen:
            common = 0
            for morpheme in inputPosCount:
                if morpheme in sentencePosCount:
                    common += min(inputPosCount[morpheme],
                                  sentencePosCount[morpheme])
                    similarity = 100 * common / inputLen
                    sentenceDict[line] = similarity
        else:
            common = 0
            for morpheme in inputPosCount:
                if morpheme in sentencePosCount:
                    common += min(inputPosCount[morpheme],
                                  sentencePosCount[morpheme])
                    similarity = 100 * common / sentenceLen
                    sentenceDict[line] = similarity

    return sentenceDict


def main(sen, File, Num):
    sentenceList = openFile(File)
    start = time.time()

    komoResult = konlpykomo(sen, sentenceList)
    komoResult = sorted(komoResult.items(), key=lambda x: x[1], reverse=True)

    for i in range(Num):
        print(f'{komoResult[i][0]} : {komoResult[i][1]}%')

    end = time.time()
    elaspedTime = end - start
    print(f'elsaped Time : {elaspedTime}s')


if __name__ == "__main__":
    inputFile = 'sample.txt'
    sentence = input('Enter a sentece >> ')
    extractNum = int(input('Enter the number of senteces to extract >> '))
    main(sentence, inputFile, extractNum)
