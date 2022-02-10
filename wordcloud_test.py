import json
from konlpy.tag import Okt
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from wordcloud import WordCloud
import re
from collections import Counter


def word_cloud(inputFileName, del_word):
    data = json.loads(open(inputFileName, 'r', encoding='utf-8').read())
    # print(data)

    post = ''

    for item in data:
        if 'description' in item.keys():
            #description 내의 문자나 숫자를 제외한 나머지를 공백으로 치환한 후
            #모든 기사의 description을 연결하여 하나의 문장으로 출력
            post = post + re.sub(r'[^\w]',' ',item['description'])+''


    #print(post)

    nlp = Okt() # Okt클래스로 객체 nlp를 생성
    post_N = nlp.nouns(post) #post에서 명사품사 추출
    # print(post_N)

    count = Counter(post_N) #단어의 빈도수를 dictionary 형태로 출력
    # print(count)
    word_count = dict() # 추출한 단어들을 저장할 빈 dict 선언
    for tag, counts in count.most_common(100):
        if len(tag) > 1: # tag(추출한 단어)의 길이가 1보다 큰 단어만 추출
            word_count[tag] = counts

    font_path = 'c:/Windows/fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    matplotlib.rc('font',family = font_name)

    del word_count[del_word]


    # print(word_count)
    plt.figure(figsize=(15,8))
    plt.xlabel('연관 키워드')
    plt.ylabel('빈도수')
    word_key = word_count.keys() #word_count에서 key만 추출
    word_value = word_count.values() #word_count에서 value 값만 추출
    plt.bar(range(len(word_count)), word_value)
    plt.xticks(range(len(word_count)), word_key, rotation=75)

    # plt.show()   # 히스토그램

    plt.figure(figsize=(10,10))
    wc = WordCloud(font_path, background_color='ivory', width =800, height = 600)
    w_colud = wc.generate_from_frequencies(word_count)
    plt.imshow(w_colud)
    plt.axis('off')

    plt.show()