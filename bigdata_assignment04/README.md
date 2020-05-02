## **[과제 4] 한글 문장의 유사도 계산 (4)
4. 문장 유사도 계산을 워드 임베딩 기법 등 다양한 방법으로 구현

- 입력: 한글 문장 1개

- 방법: 형태소 분석기 2가지와 WPM, 총 3가지 이상의 방법으로 실험

  정확도가 높은, 또는 실행 속도 빠른 방법은 무엇인지(각 방법들의 특징 또는 문제점) 비교 또는 실험 결과 설명

- 3분 내외 동영상 제작(유투브에 업로드): 구현 방법 설명 및 실행 내용

- 제출물: 소스코드 및 실행파일, 보고서(실행속도 및 실행화면 스샷 포함),

  "유투브 동영상 링크"

<참고1> 입력문장과 말뭉치의 각 문장들을 워드 임베딩 기법 등을 이용하여 문장 벡터를 만들고, 벡터 유사도 계산 기법을 이용하는 방법을 추가한 경우 가산점을 부여함.

<참고2> 실행속도를 매우 빠른 새로운 방법을 사용하여 구현한 경우에

가산점을 부여함. 멀티 쓰레딩 기법, DBMS 등 다양한 기법 사용 가능.

***

**YOUTUBE 링크**
```shell
https://youtu.be/9yDd7ApHtqA

```

**실행 결과**

![HannanumResult]("https://user-images.githubusercontent.com/62547281/79068020-a5989880-7cfe-11ea-95b6-6d05dd789b5c.png")

![KomoranResult]("https://user-images.githubusercontent.com/62547281/79068021-af220080-7cfe-11ea-9a09-e6551c331877.png")

![oktResult]("https://user-images.githubusercontent.com/62547281/79068024-b21cf100-7cfe-11ea-8dba-85c1181cb1f3.png")

***

**구현 방법**

- 형태소 분석 방식에 의한 유사도 측정
  
  아래와 같은 순서로 형태소 분석에 의한 유사도 측정 알고리즘을 구현하였다.

  1. 텍스트 파일을 한 문장씩 리스트에 저장해 반환한다.
  2. 한 문장씩 형태소를 분석한다.
  3. collections.Counter를 이용하여 각 형태소에 대한 빈도를 측정한다.
  4. 형태소 갯수가 적은 문장을 기준으로 공통 형태소 갯수를 측정한다.
  5. 입력받은 문장의 형태소 갯수로 공통 형태소 갯수를 나누고 100을 곱하여 공통 형태소 유사도를 계산하여 sentenceDict에 저장한다.
  6. 유사도가 높은 순서대로 정렬 한 후 사용자 입력으로 받은 n 만큼 문장을 출력한다.

* 1을 구현한 openFile

```python 

def openFile(filePath):
    lines = None
    with open(filePath) as f:
        try:
            lines = f.read().splitlines()
        except:
            f.close()
    return lines

```

* 2를 구현한 코드
``` python 
for line in sentenceList:
        if line == '':
            continue
        sentencePos = han.pos(line)

```

* 3을 구현한 코드
``` python 

sentencePosCount = Counter(sentencePos)

```

* 4를 구현한 코드
``` python 
common = 0
  for morpheme in inputPosCount:
    if morpheme in sentencePosCount:
      common += min(inputPosCount[morpheme],sentencePosCount[morpheme])

```

* 5를 구현한 코드
``` python 

similarity = 100 * common / inputLen
sentenceDict[line] = similarity

```

* 6을 구현한 코드
``` python 
hanResult = konlpyHannanum(sen, sentenceList)
hanResult = sorted(hanResult.items(), key=lambda x: x[1], reverse=True)

for i in range(Num):
  print(f'{hanResult[i][0]} : {hanResult[i][1]}%')

```

**문제점**

- 공통사항 : sample.txt (15000줄)
- 실행시간 : Komoran > Okt > Hannanum

1. Komoran KoNLPy 패키지의 경우 다른 형태소분석기보다 실행시간이 적게 걸렸으나 다르게 같은 입력 문장이더라도 105%의 유사도를 반환하였다.

``` shell

oktResult = [('반성은', 'Noun'), ('자신', 'Noun'), ('이', 'Josa'), ('저지른', 'Verb'), ('죄', 'Noun'), ('의', 'Josa'), ('대가', 'Noun'), ('를', 'Josa'), ('조용히', 'Adjective'), ('겸허', 'Noun'), ('하게', 'Verb'), ('받아들이는', 'Verb'), ('데', 'Noun'), ('서', 'Josa'), ('출발', 'Noun'), ('한다', 'Verb')]
komoResult = [('반성', 'NNG'), ('은', 'JX'), ('자신', 'NNG'), ('이', 'JKS'), ('저지르', 'VV'), ('ㄴ', 'ETM'), ('죄', 'NNG'), ('의', 'JKG'), ('대가', 'NNG'), ('를', 'JKO'), ('조용히', 'MAG'), ('겸허', 'NNG'), ('하', 'XSV'), ('게', 'EC'), ('받아들이', 'VV'), ('는', 'ETM'), ('데', 'NNB'), ('서', 'JKB'), ('출발', 'NNG'), ('하', 'XSV'), ('ㄴ다', 'EC')]
hanResult = [('반성', 'N'), ('은', 'J'), ('자신', 'N'), ('이', 'J'), ('저지르', 'P'), ('ㄴ', 'E'), ('죄', 'N'), ('의', 'J'), ('대가', 'N'), ('를', 'J'), ('조용히', 'M'), ('겸허', 'N'), ('하', 'X'), ('게', 'E'), ('받', 'P'), ('아', 'E'), ('들이', 'P'), ('는', 'E'), ('데', 'N'), ('서', 'J'), ('출발', 'N'), ('하', 'X'), ('ㄴ다', 'E')]

```
2. 지나치게 느린 실행시간 