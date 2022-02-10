import datetime



def getPostData(post, jsonResult):
    title = post['title'] #기사제목 추출
    description = post['description'] #기사요약 추출
    org_link = post['originallink'] #기사 오리지널 링크(신문사링크) 추출
    link = post['link'] #네이버기사 링크 추출
    pubDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900') #'Thu, 10 Feb 2022 09:14:00 +0900' 기사 추출
    pubDate = pubDate.strftime('%Y-%m-%d %H:%M:%S') #ex)2022-02-10 10:14:11

    jsonResult.append({'title': title, 'description' : description,'org_link' : org_link,
                       'link':link,'pDate' : pubDate})

