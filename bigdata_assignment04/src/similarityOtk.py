from konlpy.tag import Okt
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


def konlpyOkt(inputSentence: str, sentenceList: list) -> dict:
    okt = Okt()
    sentenceDict = dict()

    inputPos = okt.pos(inputSentence)
    inputPosCount = Counter(inputPos)
    inputLen = len(inputPosCount)

    for line in sentenceList:
        if line == '':
            continue
        sentencePos = okt.pos(line)
        sentencePosCount = Counter(sentencePos)
        sentenceLen = len(sentencePosCount)

        if sentenceLen >= inputLen:
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

    oktResult = konlpyOkt(sen, sentenceList)
    oktResult = sorted(oktResult.items(), key=lambda x: x[1], reverse=True)

    for i in range(Num):
        print(f'{oktResult[i][0]} : {oktResult[i][1]}%')

    end = time.time()
    elaspedTime = end - start
    print(f'elsaped Time : {elaspedTime}s')


if __name__ == "__main__":
    inputFile = 'sample.txt'
    sentence = input('Enter a sentece >> ')
    extractNum = int(input('Enter the number of senteces to extract >> '))
    main(sentence, inputFile, extractNum)
