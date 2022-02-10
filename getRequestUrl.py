import urllib.request


def getRequestUrl(url):

    client_id = 'NR_ryBfTZsFcSGzKYOSE'  # 네이버 api key
    client_secret = 'AiLgXALo8U'  # 네이버 api secret key

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