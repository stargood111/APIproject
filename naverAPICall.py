import urllib.request
import json
import datetime
import time

client_id = 'NR_ryBfTZsFcSGzKYOSE' # 네이버 api key
client_secret = 'AiLgXALo8U' # 네이버 api secret key

def getRequestUrl(url):
    req = urllib.request.Request(url) # 네이버서버에 보낼 요청객체를 생성
    req.add_header("X-Naver-Client-Id",client_id) # 위에서 만들어진 요청객체에 client_id를 포함시킴
    req.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(req) # 네이버서버에 요청객체 req를 전달하여 응답을 받아 response에 저장
        if response.getcode() == 200: # 응답 코드가 200정상 호출
            print('호출 성공 !!')
            ret = response.read().decode('utf-8')
            return ret
    except:
        # print('호출 에러 - 호출에러코드:',response.getcode())
        # print('에러발생 주소',url)
        print('더 이상 가져올 데이터가 없거나 호출에 에러가 발생했습니다')
        return None

def getNaverSearch (node, srcText, start, display):
    baseUrl = "https://openapi.naver.com/v1/search" #네이버 기본api 주소
    node = "/%s.json" % node
    param = "?query=%s&start=%s&display=%s"%(urllib.parse.quote(srcText), start, display)
    api_url = baseUrl + node  + param
    responseDecode = getRequestUrl(api_url)  # 호출성공시 응답받은 데이터를 저장
    if(responseDecode) == None:
        return None
    else:
        return json.loads(responseDecode)


def getPostData(post, jsonResult):
    title = post['title'] #기사제목 추출
    description = post['description'] #기사요약 추출
    org_link = post['originallink'] #기사 오리지널 링크(신문사링크) 추출
    link = post['link'] #네이버기사 링크 추출
    pubDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900') #'Thu, 10 Feb 2022 09:14:00 +0900' 기사 추출
    pubDate = pubDate.strftime('%Y-%m-%d %H:%M:%S') #ex)2022-02-10 10:14:11

    jsonResult.append({'title': title, 'description' : description,'org_link' : org_link,
                       'link':link,'pDate' : pubDate})



def main():
    node = 'news' # 검색카테고리를 news로 설정
    jsonResult=[]
    srcText = input('원하시는 검색어를 입력하세요:') # 검색어를 입력
    jsonResponse = getNaverSearch(node,srcText, 1, 100) # news 카테고리에서 입력된 검색어가 들어간 뉴스를 1~100개 추출하여 응답
    print(jsonResponse['total'])
    total = jsonResponse['total']

    count = 0

    while((jsonResponse !=None) and (jsonResponse['display'] !=0 )):
        for post in jsonResponse['items']: #응답된 json에서 기사를 추출
            count = count + 1
            getPostData(post, jsonResult)

        start = jsonResponse['start'] + jsonResponse['display']
        jsonResponse = getNaverSearch(node, srcText, start, 100)

    try:
        with open('%s_naver_%s.json' %(srcText, node),'w',encoding='utf-8') as outfile:
          jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
          outfile.write(jsonFile)
        print('파일 출력에 성공하였습니다')
    except:
        print('파일출력 에러가 발생하였습니다')

    print('전체 검색 기사 건수:', total)
    print('전체 출력 건수:', count)

if __name__ == '__main__':
    main()