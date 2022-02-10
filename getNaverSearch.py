import urllib.request
import json
import getRequestUrl





def getNaverSearch (node, srcText, start, display):
    baseUrl = "https://openapi.naver.com/v1/search" #네이버 기본api 주소
    node = "/%s.json" % node
    param = "?query=%s&start=%s&display=%s"%(urllib.parse.quote(srcText), start, display)
    api_url = baseUrl + node  + param
    responseDecode = getRequestUrl.getRequestUrl(api_url)  # 호출성공시 응답받은 데이터를 저장
    if(responseDecode) == None:
        return None
    else:
        return json.loads(responseDecode)