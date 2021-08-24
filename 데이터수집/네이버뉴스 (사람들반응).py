import requests
import json

oid = '001'
aid = '0012604850'

params = {
    'suppress_response_codes': True
    #,'callback': 'jQuery1124005705702844427485_1629261815444'
    ,'q': f'''NEWS[ne_{oid}_{aid}]|NEWS_SUMMARY[{oid}_{aid}]|JOURNALIST[76236(period)]|NEWS_MAIN[ne_{oid}_{aid}]'''
    ,'isDuplication': False
    ,'_':1629261815445
}

response = requests.get('https://news.like.naver.com/v1/search/contents',
                        params=params)

data = json.loads(response.text)
result = []
for d in data['contents'][0]['reactions']:
    result.append({
        d['reactionType']:d['count']
    })
print(result)