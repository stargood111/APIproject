import requests
from urllib import parse

base_url = "http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/"
api_key = "Rb9oYAs8K9t2c4sskY2kudyS7pTZXjq5856l1EZXeqnNKXN1RrFyzenPwHeMh0dd90Ba9CZVJwWZlJToAn9VMg=="

url_holiyday = base_url + 'getRestDeInfo'


params = {'ServiceKey':api_key,
          'solYear':2022,
          'numOfRows':100
}

response = requests.get(url_holiyday,params)
print(response.text)