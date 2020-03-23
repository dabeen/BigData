# 유사도 = (공통음절/어절개수) / (짧은문장의 음절/어절개수)

import re


def main():
    text1 = input('Input first hangul sentence >> ')
    text2 = input('Input second hangul sentence >> ')

    print(
        f'Similarity by the number of common syllables: {Syllable_similarity(text1, text2)}%'
    )
    print(
        f'Similarity by the number of common segments: {Segment_similarity(text1, text2)}%'
    )


def clean_text(text: str) -> str:
    return re.sub('[.,!?~ㆍ:/\"\']', '', text.strip())  # 문장부호 제거


def Syllable_similarity(text1: str, text2: str) -> float:

    from collections import Counter

    text1, text2 = clean_text(text1), clean_text(text2)

    text1 = ''.join(text1.split())
    text2 = ''.join(text2.split())

    if len(text1) > len(text2):
        return Syllable_similarity(text2, text1)

    syllable_count1 = dict(Counter(text1))
    syllable_count2 = dict(Counter(text2))

    commonness = 0

    for syllable in syllable_count1:
        if syllable in syllable_count2:
            commonness += min(syllable_count1[syllable],
                              syllable_count2[syllable])

    return 100 * commonness / len(text1)


def Segment_similarity(text1: str, text2: str) -> float:

    from collections import Counter

    text1, text2 = clean_text(text1), clean_text(text2)

    segments1, segments2 = text1.split(), text2.split()

    if len(segments1) > len(segments2):
        return Segment_similarity(text2, text1)

    segment_count1 = dict(Counter(segments1))
    segment_count2 = dict(Counter(segments2))

    commonness = 0

    for segment in segment_count1:
        if segment in segment_count2:
            commonness += min(segment_count1[segment], segment_count2[segment])

    return 100 * commonness / len(segments1)


if __name__ == "__main__":
    main()
