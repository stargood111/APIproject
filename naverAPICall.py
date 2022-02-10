import urllib.request
import json
import datetime
import time
import getNaverSearch
import getRequestUrl
import getPostData
import wordcloud_test

def main():
    node = 'news' # 검색카테고리를 news로 설정
    jsonResult=[]
    srcText = input('원하시는 검색어를 입력하세요:') # 검색어를 입력
    jsonResponse = getNaverSearch.getNaverSearch(node,srcText, 1, 100) # news 카테고리에서 입력된 검색어가 들어간 뉴스를 1~100개 추출하여 응답
    print(jsonResponse['total'])
    total = jsonResponse['total']

    count = 0

    while((jsonResponse !=None) and (jsonResponse['display'] !=0 )):
        for post in jsonResponse['items']: #응답된 json에서 기사를 추출
            count = count + 1
            getPostData.getPostData(post, jsonResult)

        start = jsonResponse['start'] + jsonResponse['display']
        jsonResponse = getNaverSearch.getNaverSearch(node, srcText, start, 100)

    try:
        with open('%s_naver_%s.json' %(srcText, node),'w',encoding='utf-8') as outfile:
          jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
          outfile.write(jsonFile)
        print('파일 출력에 성공하였습니다')
    except:
        print('파일출력 에러가 발생하였습니다')

    print('전체 검색 기사 건수:', total)
    print('전체 출력 건수:', count)

    file_name = '%s_naver_%s.json' % (srcText, node)
    del_word = srcText
    wordcloud_test.word_cloud(file_name, del_word)


if __name__ == '__main__':
    main()