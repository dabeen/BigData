## **과제 1** 한글 문장의 유사도 계산 (1)

1. 한글 문장의 유사도 계산 (1)
   
  - 입력: 한글 문장 2개 (매우 유사하거나 또는 약간 유사한 문장)
  - 출력: 유사도 %
  - 방법: 공통 음절 개수, 공통 어절 개수 등에 의한 유사도 계산

<참고 1> 위 과제 수행에 사용하는 언어는 C/C++, 자바, 파이썬 등 각자 사용하기 편한 언어를 사용하면 됩니다.

<참고 2> 과제 제출 내용: 소스코드, 보고서 (PDF 파일: 구현 방법 미 실행 화면 스샷 등의 설명 포함) -> zip 파일 1개로 업로드

***

**실행 결과**

![result](https://user-images.githubusercontent.com/62547281/77312234-fa22a680-6d44-11ea-8966-2095bd1bd8e1.png)


**RUN**

```shell
$ make
```

***

**구현 방법**

- 공통 음절 개수에 의한 유사도 측정

  아래와 같은 순서로 공통 음절 유사도 측정 알고리즘을 구현하였다.

  1. 입력받은 문장의 문장부호와 공백을 제거한다.
  2. collections.Counter를 이용하여 각 text에 대한 음절 빈도를 측정한다.
  3. 음절 갯수가 짧은 문장을 기준으로 공통 음절 갯수를 측정한다.
  4. 짧은 문장의 음절 갯수로 공통 음절 갯수를 나누고 100을 곱하여 공통 음절 유사도를 계산하여 반환한다.

  * 1을 구현한 clean_text
  ```python
  def clean_text(text: str) -> str:
    return re.sub('[.,!?~ㆍ:/\"\']', '', text.strip())
  ```
  * 2를 구현한 코드
  ```python
  from collections import Counter

  syllable_count1 = dict(Counter(text1))  
  syllable_count2 = dict(Counter(text2))
  ```
  * 3을 구현한 코드
  ```python
  for syllable in syllable_count1:
        if syllable in syllable_count2:
            commonness += min(syllable_count1[syllable], syllable_count2[syllable])
  ```
  * 4를 구현한 코드
  ```python
  return 100 * commonness / len(text1)
  ```
  
  

- 공통 어절 개수에 의한 유사도 측정
  
  아래와 같은 순서로 공통 어절 유사도 측정 알고리즘을 구현하였다.

  1. 입력받은 문장의 문장부호와 공백을 제거한다.
  2. colletcitons.Counter를 이용하여 각 text에 대한 어절 빈도를 측정한다.
  3. 어절 갯수가 짧은 문장을 기준으로 공통 어절 갯수를 측정한다.
  4. 짧은 문장의 어절 갯수로 공통 어절 갯수를 나누고 100을 곱하여 공통 어절 유사도를 계산하여 반환한다.
  

  * 1을 구현한 clean_text
  ```python
  def clean_text(text: str) -> str:
    return re.sub('[.,!?~ㆍ:/\"\']', '', text.strip())
  ```

  * 2를 구현한 코드
  ```python
  from collections import Counter

  segment_count1 = dict(Counter(segments1))
  segment_count2 = dict(Counter(segments2))
  ```

  * 3을 구현한 코드
  ```python
  for segment in segment_count1:
        if segment in segment_count2:
            commonness += min(segment_count1[segment], segment_count2[segment])
  ```

  * 4를 구현한 코드
  ```python
  return 100 * commonness / len(segments1)
  ```
